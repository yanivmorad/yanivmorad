import string

#
# class AlphabetIterator:
#     def __init__(self,alphbet):
#         self.alphbet = alphbet
#         if   self.alphbet not in string.ascii_letters:
#             raise Exception("")
#         if self.alphbet in string.ascii_uppercase:
#             self.list_alphbet = string.ascii_uppercase
#         if self.alphbet in string.ascii_lowercase:
#             self.list_alphbet = string.ascii_lowercase
#     def __iter__(self):
#          return index = 1+self.list_alphbet.find(self.alphbet)
#
#     def __next__(self):
#         index = self.__iter__ += 1
#         if self.index < 26:
#             return self.iterable[self.index]
#         else:
#             raise StopIteration
#         if len(string.ascii_lowercase) <= index:
#
#             return string.ascii_lowercase[index]
#         else:
#             raise StopIteration


x = AlphabetIterator("a")
# for i in x:
#     print(i)
# a = string.ascii_lowercase.index("a")
# print(a)