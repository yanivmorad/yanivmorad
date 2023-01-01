import csv

path = "AAPL.csv"

def process_stock_prices(stock_file):
    years = []
    with open(stock_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Date'].split("-")[2] in years:
                pass
            else:
                years.append(row['Date'].split("-")[2])

    data_years = {}
    with open(stock_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for i in years:
            high = []
            low = []
            volume = []
            data_years[i] = {"high": high, "low": low, "volume": volume}
            for row in reader:
                if row["Date"].split("-")[2] == i:
                    high.append(float(row["High"]))
                    low.append(float(row["Low"]))
                    volume.append(int(row["Volume"]))
                else:
                    break

    with open('../files/apple_stock_year.csv', 'w', newline='') as file:
        fieldnames = ["Year",  'Avg Price', "Min Price", "Max Price", "Avg Volume", 'Min Volume', 'Max Volume']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        for k,row in data_years.items():
            avg_price =  ((sum(row["high"])/len(row["high"])) + (sum(row["low"])/len(row["low"])))/2
            min_price = min(row["low"])
            max_price = max(row["high"])
            avg_volume = (sum(row["volume"])) / (len(row["volume"]))
            min_volume = min(row["volume"])
            max_volume = max(row["volume"])
            writer.writerow({"Year": k, 'Avg Price': avg_price, "Min Price":min_price, "Max Price":max_price,
                            "Avg Volume":avg_volume, 'Min Volume':min_volume, 'Max Volume':max_volume})







a = process_stock_prices(path)
print(a)


