# import string
#
# def find_index(list_low):
#     return map(string.ascii_lowercase.find,list_low)
#
#
# def alphbet(list_alphbet):
#     for i in list_alphbet:
#         if not i in string.ascii_letters:
#             raise Exception("only char")
#     lower = list(map(str.lower, list_alphbet))
#     return list(map(string.ascii_lowercase.find, lower))



#
# f= filter(str.islower,["1","a","3"])
# print(list(f))

t = [
    (5,7),
    (3,6)
]
print(sorted(t,key=lambda x: (x[1])))

s = ["yaggggg","fdsg","tbrg"]
def sorted_list(string:list):
    sorted_strings = sorted(string, key=lambda x: len(x))
    return sorted_strings
print(sorted_list(s))

