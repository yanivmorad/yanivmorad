import os
import csv


def csv_data(path_file: str):
    file = path_file.split(".")
    if file[-1] == "csv":
        if os.path.exists(path_file):
            filename, file_ext = os.path.splitext(path_file)
            with open(path_file) as csvfile:
                reader = csv.DictReader(csvfile)
                amount_culum = len(next(reader))
            with open(path_file, "r") as csvfile:
                reader = csv.reader(csvfile)
                num_rows = len(list(reader))
                return f"name file: {filename}\namount column: {amount_culum}\namount row: {num_rows}"
        else:
            return False


a = csv_data("../files/apple_stock_year.csv")
print(a)
