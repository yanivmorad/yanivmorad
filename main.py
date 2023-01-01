# lucky_number = input("very nice wat is your lucky number between 1 and 9 ")
# while not lucky_number.isdigit() or 1<= int(lucky_number)>=9:
# #     print("y")
# import random
# import time
# # luxury_mael = input("Which dish in Luxury meal would you like to order?(1 ,2 ,3)")
# # while not luxury_mael in ("1", "2", "3"):
# #     luxury_mael = input("please try again")
# print(time.time())
# class Car:
#     def __init__(self, manufacturer: str, model: str,
#                  color: str, fuel_consumption: float,
#                  fuel_tank_capacity: float,
#                  year: int = None):
#         print(f"Inside __init__ of {manufacturer}")
#         self.manufacturer: str = manufacturer
#         self.model: str = model
#         self.color: str = color
#         self.fuel_consumption = fuel_consumption
#         self.fuel_tank_capacity = fuel_tank_capacity
#         self.km: int = 0
#         self.fuel: float = 0
#         self.year: int = year
#         self.maintenance:dict = {}
#
#     def __str__(self):
#         print("Inside __str__")
#         return f"{self.manufacturer} | Model: {self.model} | Year: {self.year}"
#
#     def display_dashboard(self):
#         print(f"Dashboard for {self.manufacturer} {self.model}")
#         print('====================')
#         print(f"Fuel left: {self.fuel}")
#         print(f"Km: {self.km}")
#         print('====================')
#
#     def fill_tank(self, amnt: float) -> bool:
#         print(f"Inside fill_tank, amount: {amnt}")
#         if amnt <= 0:
#             print("Non-positive amnt is not allowed")
#             return False
#         if amnt + self.fuel > self.fuel_tank_capacity:
#             print(f"Cannot fill more than the tank capacity."
#                   f"Current capacity is: {self.fuel_tank_capacity}")
#             return False
#
#         self.fuel += amnt
#         return True
#     def drive(self, km: int):
#         if self.fuel <= 0:
#             return "You have no fuel!"
#         elif self.fuel < (km/self.fuel_consumption):
#             return f"Not enough fuel for the trip... you missing {(km/self.fuel_consumption) - self.fuel}l"
#         else:
#             self.km += km
#             self.fuel -= (km/self.fuel_consumption)
#         return self.fuel
#
#     def add_maintenance(self, date, describe):
#         self.maintenance[date] = describe
#
#
#
#
#
# mazda_car = Car('Mazda', '3 Spirit', 'white',
#                 fuel_consumption=20, fuel_tank_capacity=60, year=2015)
#
# toyota_car = Car('Toyota', 'Yaris', 'red',
#                  fuel_consumption=25, fuel_tank_capacity=40, year=2022)
#
# mazda_car.display_dashboard()
# # mazda_car.fill_tank()
# # Car.fill_tank(mazda_car)
#
# is_success = mazda_car.fill_tank(20)
# mazda_car.display_dashboard()
# is_success = mazda_car.fill_tank(100)
# mazda_car.display_dashboard()
# # while not is_success:
# #   is_success = mazda_car.fill_tank(20)

import math
from datetime import datetime

# class Point2D:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def translate(self, dx, dy):
#         self.x += dx
#         self.y += dy
#
#     def __str__(self):
#         return f"({self.x},{self.y})"

#     def __eq__(self, other):
#         print("inside __eq__ of Point2D")
#         if not isinstance(other, Point2D):
#             return False
#         return self.x == other.x and self.y == other.y
#
#     def __ne__(self, other):
#         print("inside __ne__ of Point2D")
#         return self.x != other.x or self.y != other.y
#
#     def __add__(self, other):
#         new_point = Point2D(self.x + other.x,self.y + other.y)
#         return new_point
#
#
#     # def distance_from(self, other):
#     #     dx = self.__x - other.__x
#     #     dy = self.__y - other.__y
#     #     dist = math.sqrt(dx ** 2 + dy ** 2)
#     #     return dist
#     #
#     # def __str__(self):
#     #     return f"({self.__x},{self.__y})"
# if __name__ == '__main__':
#     p1 = Point2D()
#     p2 = Point2D(2, 5)
#     print(p1, p2)
#     p2.translate(-2, -2)
#     p1.translate(3, 3)
#     print(p1)
#     print(p2)
#     p3 = Point2D(0, 3)
#     print(f"p1: {p1}, p2: {p2}, p3:{p3}")
#     print(f"p2 == p3: {p2 == p3}")
#     print(f"p2 == p1: {p2 == p1}")
#     print(f"p2 != p3: {p2 != p3}")
#     print(p2 == "hello")
#     # print("hello" == 'world')
#     print(p2+p1)
#
#     # s1 = input()
    # s2 = input()
    # print(s1 == s2)
    # print(s1 is s2)

# class USDConverter:
#     def __init__(self):
#         self.exchange_rate = {}
#     def add_exchange_rate(self,currency,rate:float):
#         self.exchange_rate[currency]=rate
#     def convert(self,currency ,to_currency):
#       self.exchange_rate

# class Watter_App:
#     def __init__(self):
#         self.db = {}
#     def singup(self,user_name:str):
#         if user_name not in self.db:
#             self.db[user_name]={
#             'total cups' : 0,
#             'date dict': {}
#                 }
#     def add_cup(self,user_name , date):
#         self.db[user_name]['date dict']
#     def get_cups_per_user(self,user_name):
#         return self.db[user_name]["total cups"]

# class Customer:
#     def __init__(self, name, address, phone, email=None):
#         self.name = name
#         self.address = address
#         self.phone = phone
#         self.email = email
#
#
# class Store:
# #     def __init__(self, store_name):
# #         self.customer: {str: Customer} = {}
# #
# #     def add_customer(self, name, address, phone, email=None):
# #         new_customer = Customer(name, address, phone, email)
# #         self.customer[name] = new_customer
# #
# #     def add_qty(self):
# #         pass
# # if gfgfdg:
# #     print(vfdb)
# # elif dfer
# #     print(vdfvf):
# # else:
# #     print(dved)
#
#
#
#
#
#
#
#
#
# class Customer:
#     def __init__(self, name, address, phone, email=None):
#         self.name = name
#         self.address = address
#         self.phone = phone
#         self.email = email
#
#     def __str__(self):
#         return f"<Customer>\n" \
#                f"Name: {self.name}\n" \
#                f"Address: {self.address}\n" \
#                f"Phone: {self.phone}"
#
#     def __repr__(self):
#         return f"<Customer> {self.name}"
#
#
# class Product:
#     def __init__(self, sku: str, category: str, brand: str,
#                  qty: float, price: float,
#                  model: str = None,
#                  warranty_months: int = None):
#         if price <= 0:
#             pass
#             # error
#             # return None
#         self.sku = sku
#         self.category = category
#         self.price = price
#         self.qty = qty
#
#     def update_qty(self, diff: float):
#         if diff + self.qty < 0:
#             # error
#             return None
#         self.qty += diff
#
#     def update_price(self, new_price):
#         if new_price <= 0:
#             # error
#             return None
#         self.price = new_price
#
#     def __str__(self):
#         pass
#
#     def __repr__(self):
#         pass
#
#     def __eq__(self, other):
#         return self.sku == other.sku
#
#
# # c = Customer('adv', 'sdfs', 'sdfs')
# # c.phone = '054-342342'
#
# #
# # d1 = {
# #     'address':'sdfs'
# # }
# #
# # c1 = Customer()
#
# class Store:
#     def __init__(self, store_name):
#         self.store_name = store_name
#         self.customers: dict[str: Customer] = {}
#         self.inventory: {str: Product} = {}
#         self.inventory_by_name: dict[str: Product] = {}
#         # customers
#         # inventory
#         # order_product
#         # orders
#         # shipments
#
#     def add_customer(self, name, address, phone, email=None):
#         new_customer = Customer(name, address, phone, email)
#         self.customers[name] = new_customer
#
#     def add_product_to_inventory(self, sku: str, category: str, brand: str,
#                                  qty: float, price: float,
#                                  model: str = None,
#                                  warranty_months: int = None):
#         new_product = Product(sku, category, brand,
#                               qty, price, model, warranty_months)
#         self.inventory[sku] = new_product
#         self.inventory_by_name[brand+model] = new_product
#
#     def add_qty(self, sku:str, qty: float):
#         self.inventory[sku].update_qty(qty)
#
#     def add_items(self, skus: list, quantities: list):
#         for sku, qty in zip(skus, quantities):
#             self.add_qty(sku, qty)
#
#     def get_products_by_brand(self, brand) -> list[Product]:
#         ret_val = list()
#         for product in self.inventory.values():
#             if product.brand == brand:
#                 ret_val.append(product)
#         return ret_val
#
#     def get_out_of_stock(self):
#         pass
#
#     def add_order(self):
#         pass

# d2 = "11-11-2011"
# date2 = datetime.strptime(d2, "%d-%m-%Y")
# print(date2.date())
import csv

# import pytz
#
# # d ={}
# # d["add"]["ss"]=[3,2]
# # print(d)
# utc_plus_2 = pytz.timezone('UTC+02:00')
# current_time = datetime.now(utc_plus_2)
# formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S %Z')
# print(formatted_time)
nums = [3,2,2]
nums = sorted(nums)

correct_nums = []
for i in range(1, len(nums) + 1):
    correct_nums.append(i)
for i, n in enumerate(correct_nums):
    if correct_nums[i] != nums[i]:
        print(nums[i], correct_nums[i])

def letco(nuns:list):
    nums.sort()
    missing = None
    duplicate = None
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            duplicate = nums[i]
        elif nums[i] - nums[i-1] > 1:
            missing = nums[i-1] + 1
    return [duplicate, missing]
print(letco(nums))