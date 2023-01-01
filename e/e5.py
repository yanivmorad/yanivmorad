import csv
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor

path = "../d/AAPL.csv"

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
        lines = []
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

    data_avg = []
    for k, row in data_years.items():
        avg_price = ((sum(row["high"]) / len(row["high"])) + (sum(row["low"]) / len(row["low"]))) / 2
        min_price = min(row["low"])
        max_price = max(row["high"])
        avg_volume = (sum(row["volume"])) / (len(row["volume"]))
        min_volume = min(row["volume"])
        max_volume = max(row["volume"])
        data_avg.append({"Date": k, "Low": avg_price, "Open": min_price, "Volume": max_price,
                         "High": avg_volume, "Close": min_volume, "Adjusted Close": max_volume})
    with open(stock_file) as csvfile:
        reader = csv.DictReader(csvfile)
        dict_r = []
        for i in reader:
            dict_r.append(i)


    for a in data_avg:
         if not os.path.exists("C:\example_e5"):
            os.makedirs("C:\example_e5")

         file_path = os.path.join("C:\example_e5", f"AAPL_{a['Date']}.csv")

         with open(file_path, 'w', newline='') as fh:
            writer = csv.DictWriter(fh, ["Date", "Low", "Open", "Volume", "High", "Close", "Adjusted Close"])
            writer.writeheader()
            for row in dict_r:
                if row["Date"].split("-")[2] == a["Date"]:
                 writer.writerow(row)
            writer.writerow(a)
if __name__ == '__main__':

    stat = time.time()
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(process_stock_prices, path)]
    print(time.time()-stat)
