import csv
import json
import os.path


def file_line(file_path, start_line: int, end_line: int):
    if not os.path.exists(file_path):
        raise Exception("doesn't exists")
    with open(file_path, "r") as fd:
        if type(start_line) != int or type(end_line) != int:
            raise Exception("Line number must be an integer")
        content = fd.readlines()
        if end_line > len(content) or start_line <=0:
            raise Exception("Line number out of range")
        return content[start_line - 1:end_line - 1]

def csv_check(csv_path):
    if not os.path.exists(csv_path):
        raise Exception("doesn't exists")
    if os.path.splitext(csv_path)[-1][1:] != "csv":
        raise Exception("no in format")
    with open(csv_path) as csv_file:
        content = csv.DictReader(csv_file)
        sum_row = 0
        for i in content:
            sum_row+=1
    return f"List of column names:{content.fieldnames}\n" \
           f"Number of rows in the file: {sum_row}\n" \
           f"Number of columns in the file: {len(content.fieldnames)}"


def csv2json( file_path_csv,new_json_path):
    if not os.path.exists(file_path_csv):
        raise Exception("csv file doesnt exists")
    if os.path.splitext(file_path_csv)[-1][1:] != "csv":
        raise Exception("doesnt csv")
    if os.path.splitext(new_json_path)[-1]!= ".json":
        raise Exception ("Not a valid path")
    with open(file_path_csv,"r") as fh:
        file =csv.DictReader(fh)
        json_list = list(file)
        # for i in file:
        #     json_list.append(i)
    with open(new_json_path,"w") as jf:
        json.dump(json_list,jf)

def json2csv(json_file_path,new_csv_path):
    if not os.path.exists(json_file_path):
        raise Exception("csv file doesnt exists")
    if os.path.splitext(json_file_path)[-1][1:] != "json":
        raise Exception("doesnt json")
    if os.path.splitext(new_csv_path)[-1]!= ".csv":
        raise Exception ("Not a valid path")
    with open(json_file_path,"r") as fj:
      data = json.load(fj)
    fieldnames = set()
    for i in data:
       for d in i:
            fieldnames.add(d)
    with open(new_csv_path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':

    try:
        file_line("sample2.txt", 2, 2)
        csv_check("SampleCSVFile_1.csv")
        csv2json("AAPL.csv","AAPL.json")
        json2csv("sample4.json","bal.csv")
    except Exception as e:
        print(e)
