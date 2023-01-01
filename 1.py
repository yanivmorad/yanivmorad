# class Address:
#     def __init__(self, country, city, street, house_num, flat_num):
#         self.country = country
#         self.city = city
#         self.street = street
#         self.house_num = house_num
#         self.flat_num = flat_num
#
#
# class Bathroom:
#     def __init__(self, , size, toilet, sink, bath, shower):
#         self.size = size
#         self.toilet = toilet
#         self.sink = sink
#         self.bath = bath
#         self.shower = shower
#         self.details = {}
#
#
# #
# class  Flat:
#     def __init__(self,rooms: int,kitchen_size: int,balconies,flat_size):
#         self.address: dict[Address]={}
#         self.floor = []
#         self.rooms = rooms
#         self.bathroom: dict[Bathroom] ={}
#         self.kitchen_size = kitchen_size
#         self.balconies =balconies
#         self.flat_size =flat_size
#     def add_address(self, country, city, street, house_num, flat_num):
#         new_address = Address(country, city, street, house_num, flat_num)
#         self.address[country] =new_address
#     def add_floor(self,total_floor_building: int, floor_flat: int  ):
#         self.floor = {"total_floor_building": total_floor_building,
#                       "floor_flat": floor_flat
#                       }
#     def add_bathroom(self,amount,size, toilet, sink, bath, shower):
#
#
#         def details():
#             for b in range(self.amount):
#                 details[b] = {self.size, self.toilet, self.sink, self.bath, self.shower}
# from datetime import date, datetime, timedelta,time
# print(datetime.now())
# print(timedelta(hours=2,minutes=30))
# a = datetime.now() + timedelta(hours=2,minutes=10)
# print(a - datetime.now())
