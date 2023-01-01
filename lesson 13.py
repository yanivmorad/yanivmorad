# from datetime import datetime
# from time import perf_counter
#
#
# def performance_log(func):
#     def wrapper(*args,**kwargs):
#        start = perf_counter()
#        a = func(*args,**kwargs)
#        stop = perf_counter()
#        print(stop-start)
#        return a
#
#     return wrapper
# @performance_log
# def long_running(num, iters):
#     val = 1
#     for i in range(iters):
#         val *= num
#     return val
# long_running(2,1)
#
#
# class Bank:
#
#     def __init__(self, bank_name):
#         self.name = bank_name
#
#     '''
#       Perform validation that the operation is being performed
#       during working hours only: Sun - Thu, 09:00 - 17:00
#     '''
#
#     def working_hours_only(callable):
#
#         def wrapped_callable(*args, **kwargs):
#             today = datetime.now().strftime("%A")
#             hour = datetime.now().hour
#             work_days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Sunday"]
#             if today in work_days_of_week and 9<=hour<17:
#                 ret_val = callable(*args, **kwargs)
#                 return ret_val
#             else:
#                 raise Exception("Outside working hours")
#
#         return wrapped_callable
#
#     @working_hours_only
#     def withdraw(self, amount):
#         print("Called withdraw", amount)
#         return amount
#
#     @working_hours_only
#     def deposit(self, amount):
#         print("Called deposit")
#
#     def feedback(self, fedback_text):
#         print("Called feedback")
# # day = datetime.now().strftime("%A")
# # print(day)
# #
# # print(datetime.now().hour)
# b = Bank("hpooalim")
#
# class Person:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         self._name = value
#
# person = Person('John')
# print(person.name)  # Output: 'John'
#
# person.namew = 'Jane'
# print(person.name)
# import requests
#
#
# def ingle_str_arg(func):
#     def wrapper(*args, **kwargs):
#         if len(args) == 1 and type(args[0]) == str:
#             ret_val = func(*args, **kwargs)
#             return ret_val
#         else:
#             raise Exception("InvalidArgument")
#
#     return wrapper
#
# @ingle_str_arg
# def string_1(string:str):
#     return string
#
# print(string_1("23"))
#
# def valid_param_types(valid_params:list):
#     def inner(funk):
#         def wrapper(*args, **kwargs):
#             for a in args:
#                 if type(a) in valid_params:
#                     return funk(*args, **kwargs)
#                 else:
#                     raise Exception()
#         return wrapper
#     return inner
# @valid_param_types([int,float])
# def init(num):
#     return num
from idlelib import query

import requests
#
# BORED_URL = "https://www.boredapi.com/api/activity"
# response = requests.get(BORED_URL)
# print(response)
#
# print(response.status_code)
# print(response.text)
# # print(response.text['activity']) # not working
#
# print(response.json())
#
# response = requests.get("https://bad_url")
# # response = requests.get("https://www.boredapi.com/api/act")
# print(response.status_code)
# print(response.text)
#

# with query param
#
# GENDERIZE_URL = "https://api.genderize.io/"
# response = requests.get(GENDERIZE_URL, params={'name': 'valeria'})
# print(response.status_code, response.text, sep="\n")
#
# GENDERIZE_URL = "https://api.genderize.io/bla/"
# response = requests.get(GENDERIZE_URL, params={'name': 'valeria'})
# print(response.status_code, response.text, sep="\n")
#
# {"country": [{"country_id": "GH", "probability": 0.224}, {"country_id": "PH", "probability": 0.084},
#              {"country_id": "NG", "probability": 0.073}, {"country_id": "US", "probability": 0.061},
#              {"country_id": "NE", "probability": 0.034}], "name": "nathaniel"}
#
#
# with path param
# https://restcountries.com/v3.1/alpha/il
# if __name__ == '__main__':
 # name = input("insert your name" )
 # Nationalize_by_name = "https://api.nationalize.io/?"
 # response = requests.get(Nationalize_by_name, params={'name': name})
 # if response.status_code > 400:
 #  raise Exception("this name does not exist")
 # # print(response.json()['country'])
 # l = []
 # for i in response.json()['country']:
 #   l.append(i['probability'])
 # for i in response.json()['country']:
 #  if max(l) == i['probability']:
 #   country = i['country_id']
 # # print(country)
 #
 # CountryRest = f"https://restcountries.com/v3.1/alpha/{country}"
 # respo =  requests.get(CountryRest)
 # if respo.status_code  > 400:
 #  raise Exception ("404")
 # # print(respo.json())
 # for i in respo.json():
 #  ful_contry_name = i['name']['common']
 # print(f"your name from {ful_contry_name} ")
# def sconde(list):
#     large = None
#     scendr = None
#     for i in list:
#         if large == None:
#             large =i
#
#         elif i >large:
#             scendr = large
#             large =i
#         elif scendr < i < large:
#              scendr = i
#     return scendr
# s = sconde([321,32,43,5,67,78,34,1,3,65,54,3,3])
# print(s)

