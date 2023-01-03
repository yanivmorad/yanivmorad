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


if __name__ == '__main__':

    try:
        file_line("", 1, 10)
    except Exception as e:

        print(e)
