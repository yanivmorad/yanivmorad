from datetime import datetime


class RavKav:
    rides = {'short': {'range': (0, 15), 'price': 5.5},
             'medium': {'range': (16, 40), 'price': 12},
             'long': {'range': (40, 1000), 'price': 23},
             }

    def __init__(self, holder_id, holder_name):
        self.__holder_id = holder_id
        self.__holder_name = holder_name
        self.__balance = 0
        self.__rides_log_in_date = {

        }

    def get_log_date(self):
        return self.__rides_log_in_date

    def topup(self, amount_money):
        if amount_money > 0:
            self.__balance += amount_money
        else:
            return False

    def ride(self, amount_km: int, date: datetime.date):
        for type_ride, ride_details in self.rides.items():
            if ride_details["range"][0] <= amount_km <= ride_details["range"][1]:
                pay_ride = ride_details["price"]
                if self.__balance < pay_ride:
                    return False
                else:
                    self.__balance -= pay_ride
                    date_n = datetime.strptime(date, "%d-%m-%Y").date()
                    self.__rides_log_in_date[date_n] = [type_ride]


a = RavKav("yaniv", "moradifar")
a.topup(1000)
a.ride(12, "12-12-2022")
a.ride(50, "11-11-2021")
a.ride(2, "11-12-2011")
a.ride(500, "11-12-2011")
print(a.get_log_date())


    # def ride(self ,amount_ride_km: int):
    #     if amount_ride_km <= 15:
    #        if self.__balance < 5.5:
    #            return False
    #        else:
    #            self.__balance -= 5.5
    #            self.__rides_log[datetime.now().date()] = amount_ride_km
    #     elif amount_ride_km <= 40:
    #         if self.__balance < 12:
    #             return False
    #         else:
    #             self.__balance -= 12
    #             self.__rides_log = {"date":datetime.now().date(),"ride type" :
    #             "medium" ,"km_ride" : amount_ride_km}
    #         if self.__balance < 23:
    #             return False
    #         else:
    #             self.__balance -= 23
    #             self.__rides_log[datetime.now().date()] = amount_ride_km
