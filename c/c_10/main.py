import abc
import csv
import json
import os.path
from abc import ABC


class TextFile(ABC):
    def __init__(self, file_path):
        if not os.path.exists(file_path):
            raise Exception("doesn't exists")
        if os.path.splitext(file_path)[-1][1:] != self._get_ext():
            raise Exception("no in format")
        self._file_path = file_path

    def get_file_size(self):
        size = os.path.getsize(self._file_path)
        dir1, name = os.path.split(self._file_path)
        return f"The size of the {name} file is:{size} "

    def get_content(self):
        with open(self._file_path, 'r') as fd:
            content = self._get_specific_content(fd)
            return content

    @abc.abstractmethod
    def _get_specific_content(self, fd):
        pass

    @abc.abstractmethod
    def _get_ext(self):
        pass


class CsvFile(TextFile):
    def __init__(self, file_path, delimiter=','):
        super().__init__(file_path)
        self._delimiter = delimiter

    def _get_ext(self):
        return 'csv'

    def _get_specific_content(self, fd):
        ret_val = []
        for row in csv.DictReader(fd, delimiter=self._delimiter):
            ret_val.append(row)
        return ret_val
    def __add__(self, other):
        header1 = dict(self.get_content()[0]).keys()
        header2 = dict(other.get_content()[0]).keys()
        if header1 == header2:
            concatenated = self.get_content() + other.get_content()
            dir1, name1 = os.path.split(self._file_path)
            dir2, name2 = os.path.split(other._file_path)
            new_name = f"{name1.split('.')[0]}_{name2.split('.')[0]}.csv"
            new_path = os.path.join(dir1, new_name)
            fieldnames = header2

            with open(new_path, 'w',newline="") as f:
                writer = csv.DictWriter(f,fieldnames=fieldnames)
                writer.writeheader()
                for i in concatenated:
                    writer.writerow(i)


            return CsvFile(new_path)
        else:
            raise Exception("the header not even")



class JsonFile(TextFile):
    def _get_ext(self):
        return 'json'

    def _get_specific_content(self, fd):
        return json.load(fd)




class TxtFile(TextFile):

    def _get_ext(self):
        return 'txt'

    def _get_specific_content(self, fd):
        return fd.read()

    def __add__(self, other):
        concatenated = self.get_content() + other.get_content()
        dir1, name1 = os.path.split(self._file_path)
        dir2, name2 = os.path.split(other._file_path)
        new_name = f"{name1.split('.')[0]}_{name2.split('.')[0]}.txt"
        new_path = os.path.join(dir1, new_name)
        with open(new_path, 'w') as f:
            f.write(concatenated)

        return TxtFile(new_path)

if __name__ == '__main__':
    try:
        txt_1 = TxtFile("sample2.txt")
        txt_2 =TxtFile("sample3.txt")
        print(txt_1.get_file_size())
        # print(d.get_content())
        new_txt = txt_1 +txt_2
        print(new_txt.get_file_size())
        csv_1 = CsvFile("SampleCSVFile_1.csv")
        csv_2= CsvFile("SampleCSVFile_2.csv")
        print(csv_1.get_file_size())
        new_csv = csv_1+csv_2
        print(new_csv.get_file_size())
        json_1 = JsonFile("sample4.json")
        json_2 = JsonFile("sample1.json")
    except Exception as e:
        print(e)
