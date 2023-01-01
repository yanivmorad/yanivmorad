import os
import pickle


class ScheduledRide:
    counter = 0
    def __init__(self,line_number, origin_time, destination_time, driver_name):
        self.line_number = line_number
        ScheduledRide.counter += 1
        self.ride_id = self.counter
        self.origin_time = origin_time
        self.destination_time = destination_time
        self.driver_name = driver_name
        self.delays = 0

    def __str__(self):
        return f"Ride ID: {self.ride_id}, Line number: {self.line_number}" \
               f", The origin time: {self.origin_time}, Destination time {self.destination_time}" \
               f", Driver name: {self.driver_name}"

    def __repr__(self):
        return f"Ride ID: {self.ride_id}, Line number: {self.line_number}, The origin time:" \
               f" {self.origin_time}, Destination time {self.destination_time}, Delays: {self.delays}"
    def _get_info_by_line_number(self, line_number):
        ride_num = None
        if self.line_number == line_number:
            ride_num = self.ride_id
        return ride_num
    def _delay(self):
        self.delays += 1
        print(f"Your request has been approved \n {self.delays} minutes")



class BusRoute:
    def __init__(self, line_number, origin, destination, stops):
        self.line_number = line_number
        self.origin = origin
        self.destination = destination
        self.stops = stops
        self.scheduled_rides: {str: ScheduledRide} = []

    def __str__(self):
        return f"\nLine number: {self.line_number},\n" \
               f"The origin - destination: {self.origin} - {self.destination},\n" \
               f"Stops: {self.stops} \n {self.scheduled_rides}"

    def __repr__(self):
        return f"\nLine number: {self.line_number},\n" \
               f"The origin - destination: {self.origin} - {self.destination}, Stops: {self.stops}\n"

    def _scheduled_ride(self,new_schedule):
        self.scheduled_rides.append(new_schedule)

    def _update_origin(self, change_to):
        self.origin = change_to

    def _update_destination(self, change_to):
        self.destination = change_to

    def _update_stops(self, change_to):
        self.stops = change_to

    def _del_scheduled(self,ride_id):
        self.scheduled_rides.pop(ride_id)

    def _search_routes(self, user_input):
        for i in self.__dict__.values():
            if isinstance(i, list):
                for k in i:
                    if k == user_input:
                        return self.line_number
            if i == user_input:
                return self.line_number






class BestBusCompany:
    def __init__(self):
        self.routes: {int:BusRoute} = {}
        self.schedules: {int: ScheduledRide} = {}

    def __str__(self):
        return f"Route number {self.routes}"

    def add_route(self, line_number, origin, destination, stops):
        new_route = BusRoute(line_number, origin, destination, stops)
        self.routes[line_number] = new_route

    def remove_route(self, line_number):
        if line_number in self.routes:
            answer = input(f"Are you sure you want to delete line {line_number}? (Yes or no)")
            if answer.lower() == "yes":
                self.routes.pop(line_number)
                print(f"Line {line_number} was successfully deleted")

    def update_route(self, line_number):
        if line_number in self.routes:
            print(self.routes[line_number])
            kye_change = input("what you want to change origin, destination, stops ")
            while not kye_change in ("origin", "destination", "stops"):
                kye_change = input("please try again, what you want to change origin, destination, stops ")
            change_to = input(f"enter the new{kye_change}: ")
            if kye_change == "origin":
                self.routes[line_number]._update_origin(change_to)
            if kye_change == "destination":
                self.routes[line_number].update_destination(change_to)
            if kye_change == "stops":
                self.routes[line_number].update_stops(change_to)
            print(self.routes[line_number])


    def add_scheduled_ride(self, line_number):
        l = []
        ret_val = None
        for i in self.schedules.keys():
            ret_val = self.schedules[i]._get_info_by_line_number(line_number)
            if not ret_val == None:
                l.append(ret_val)
        if len(l) == 0:
            print("There not schedule rides for this line.")
        else:
            for i in l:
                print(self.schedules[i])
        origin_time = input(" please enter the origin time fo this ride ")
        destination_time = input("please enter the destination time time fo this ride")
        driver_name = input("please enter the driver name time fo this ride")
        new_scheduled = ScheduledRide(line_number, origin_time, destination_time, driver_name)
        self.schedules[new_scheduled.ride_id] = new_scheduled
        self.routes[line_number]._scheduled_ride(new_scheduled)

    def remove_schedules(self, ride_id):
        if ride_id in self.schedules:
            self.schedules.pop(ride_id)
        if ride_id in self.routes:
            self.routes[ride_id]._del_scheduled(ride_id)

    def search_route(self, user_input):
        l = []
        ret_val = None
        for i in self.routes.keys():
            ret_val = self.routes[i]._search_routes(user_input)
            if not ret_val == None:
                l.append(ret_val)
        if len(l) == 0:
            print("No ride found for your request")
        else:
            for j in l:
                print(self.routes[j])
                print()


    def report_delay(self, user_input):
        l = []
        ride_num_list = []
        ret_val = None
        for i in self.routes.keys():
            ret_val = self.routes[i]._search_routes(user_input)
            if not ret_val == None:
                l.append(ret_val)
        for k in l:
            for j in self.schedules.keys():
                ret_val = self.schedules[j]._get_info_by_line_number(k)
                if not ret_val == None:
                    ride_num_list.append(ret_val)
        for i in ride_num_list:
            print(self.schedules[i])
        if len(l) == 0:
            print("No ride found for your request")
        else:
            which_ride = input("Please select which ride you want to report as late (enter the ID ride): ")
            self.schedules[int(which_ride)]._delay()


def is_digit(number:str):
    while not (number.isdigit()) or int(number) < 0:
        number = input("pleas enter integer number ")
    return number

if __name__ == '__main__':
    if not os.path.exists('bus_company.pickle'):
        eged = BestBusCompany()

    else:
        with open('bus_company.pickle', 'rb') as fh:
            eged = pickle.load(fh)

            while True:
                user = input(f"please choose what are you manger or passenger:\n"
                             f"if you want exit press 0")
                while not user in ("manger","passenger","0"):
                    user = input("please choose what are you (manger/passenger):")
                if user == "manger":
                    flag = False
                    for i in range(3):
                        password = input("please entre password" )
                        if password == "1":
                            flag = True
                            break
                    if not flag:
                        raise Exception("You were kicked out of the program because you got your password wrong three times ")
                    while True:
                        print()
                        manager_actions=input(f"hello manger What action would you like to do?"
                          f"\n1) add route\n2) delete route\n3) update route\n4) add scheduled ride\n"
                                              f"5) remove schedules\n0) to get out of the system ")
                        if manager_actions == "1":
                            line_number =is_digit( input("enter line number"))
                            origin = input("origin ")
                            destination = input("destination ")
                            stops = input("List of stops separated by a comma(,)").split(",")
                            eged.add_route(int(line_number), origin, destination, stops)
                        elif manager_actions == "2":
                            line_number =is_digit(input("enter line number"))
                            eged.remove_route(int(line_number))
                        elif manager_actions == '3':
                            line_number = is_digit(input("enter line number"))
                            eged.update_route(int(line_number))
                        elif manager_actions =="4":
                            line_number = is_digit(input("enter line number"))
                            eged.add_scheduled_ride(int(line_number))
                        elif manager_actions == "5 ":
                            ride_id = is_digit(input("please enter ride ID "))
                            eged.remove_schedules(int(ride_id))
                        elif manager_actions== "0":
                            break
                elif user == "passenger":
                    while True:
                        print()
                        print("welcome to eged the best bus ever")
                        passenger_actions = input("What action would you like to do? Enter the desired number\n1) search_route"
                                                  "\n2) report_delay\n0) to get out of the system")
                        if passenger_actions == "1":
                           search_line =input("please enter the line you want search."
                                              " if you want a search by origin,destination,stops press a ")
                           if search_line =="a":
                                search = input("pleease enter the origin,destination,stops")
                                eged.search_route(search)
                           else:
                               line = is_digit(search_line)
                               eged.search_route(int(line))
                        elif passenger_actions == "2":
                            report_line = input("please enter the line you want to report."
                                                " if you want a search by origin,destination,stops press a ")
                            if report_line == "a":
                                search = input("pleease enter the origin,destination,stops")
                                eged.report_delay(search)
                            else:
                                line = is_digit(report_line)
                                eged.report_delay(int(line))
                        elif passenger_actions == "0":
                            print()
                            print("Thank you very much for traveling with us, we look forward to seeing you later")
                            print()
                            break
                elif user == "0":
                    break



    with open('bus_company.pickle', 'wb') as fh:
        pickle.dump(eged, fh)



