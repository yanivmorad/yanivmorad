import json

import psycopg2
from flask import Flask, request, jsonify

app = Flask("bank_web_app")

# bank REST api
# get /customers
# get /customers/id

conn = psycopg2.connect(
    host="localhost",
    port=1212,
    database="bank",
    user="postgres",
    password="yaniv1212")


@app.route("/api/v1/customers/<int:customer_id>", methods=['GET'])
def get_customer_per_id(customer_id):
    print(f"called /customers/customer_id/{customer_id}")
    with conn:
        with conn.cursor() as cur:
            sql = "SELECT * FROM customers WHERE id = %s"

            cur.execute(sql,(customer_id,))
            result = cur.fetchone()
            print(result)
            if result:
                ret_data = {
                    'id': result[0],
                    'passport_num': result[1],
                    'name': result[2],
                    'address': result[3]
                }
                # option I
                # response = app.response_class(
                #     response=json.dumps(ret_data),
                #     status=200,
                #     mimetype='application/json'
                # )
                # return response

                # option II
                return jsonify(ret_data)
            else:
                return app.response_class(
                    status=404
                )

@app.route('/api/v1/customers', methods=['GET'])
def get_customer():
    passport_num = request.args.get('passport_num')
    name = request.args.get('name')
    address = request.args.get('address')

    query = "SELECT * FROM customers WHERE 1=1"
    if passport_num:
        query += " AND passport_num='{}'".format(passport_num)
    if name:
        query += " AND name='{}'".format(name)
    if address:
        query += " AND address='{}'".format(address)
    print(query)
    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
        customers = cursor.fetchall()

        return customers


@app.route('/api/v1/customers', methods=['POST'])
def create_customer():
    passport_num = request.form['passport_num']
    name = request.form['name']
    address = request.form['address']

    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO customers (passport_num, name, address) VALUES (%s, %s, %s)",
                    (passport_num, name, address))

        conn.commit()

        return jsonify({
    "passport_num": passport_num,
    "name": name,
    "address": address
})

@app.route("/customers/<int:customer_id>", methods=['PUT'])
def update_customer(customer_id):
    new_data = request.form
    updates_str_list = []
    for field in new_data:
        updates_str_list.append(f"{field}=%s")
    sql = f"UPDATE customers SET {','.join(updates_str_list)} WHERE id=%s"
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, tuple(new_data.keys()) + tuple([customer_id]))
            if cur.rowcount == 1:
                # update succeeded
                return app.response_class(status=200)
    return app.response_class(status=500)

@app.route('/api/v1/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    with conn:

        cursor = conn.cursor()

        delete_query = 'DELETE FROM customers WHERE id = %s'
        cursor.execute(delete_query, (id,))
        conn.commit()
        count = cursor.rowcount
        if count > 0:
            return jsonify({"message": f"customer {id} deleted successfully"})
        else:
            return jsonify({"message": "customer not found"})



# running from commandline or code
# debugging
if __name__ == '__main__':
    app.run(debug=True)