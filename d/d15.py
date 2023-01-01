def ingle_str_arg(func):
    def wrapper(*args, **kwargs):
        if len(args) == 1 and type(args[0]) == str:
            ret_val = func(*args, **kwargs)
            return ret_val
        else:
            raise ValueError

    return wrapper

@ingle_str_arg
def string_1(string:str):
    return string
try:
    print(string_1(7))
except ValueError :
    print("insert string")

def valid_param_types(valid_params:list):
    def inner(funk):
        def wrapper(*args, **kwargs):
            for a in args:
                if type(a) in valid_params:

                    return funk(*args, **kwargs)
                else:
                    raise Exception("Invalid argument types")

        return wrapper

    return inner


@valid_param_types([int, float])
def init(num):
    return num

try:
    print(init(2))
except Exception as e:
    print(e)

def numeric_in_range(min_num: int,max_num:int):
    def inner(funk):
        def wrapper(*args: int, **kwargs):
            for i in args:
                if min_num<i<max_num:
                    return funk(*args, **kwargs)
                else:
                    raise Exception("number not in range")

        return wrapper

    return inner
@numeric_in_range(3,7)
def numner(num):
    return num

numner(8)