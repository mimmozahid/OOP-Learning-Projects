from bus import*
from passenger import*
from admin import*

class BusSystem:
    fare = 500

    def __init__ (self, company_name):
        self.company_name = company_name
        self.buses = []
        self.passengers = []
        self.admin = Admin ("admin", "@123")
        self.login_admin = False


    def admin_login (self, username, password) -> bool:
        if (self.admin.logIn (username, password)):
            self.login_admin = True
            return True
        return False

    def logout (self):
        self.login_admin = False

    def add_bus (self, number, route, seats):
        bus = Bus (number, route, seats)
        self.buses.append (bus)
        print ("Bus Added Successfully")
            

    def add_passenger (self, passenger):
        self.passengers.append (passenger)

    def find_bus (self, number):
        for bus in self.buses:
            if str(bus.number) == str(number):
                return bus
        return None

    def show_buses (self):
        if (len (self.buses) == 0):
            print ("---No Bus Available---")
            return
        
        print ("----Available Buses----")
        for bus in self.buses:
            print (bus)

    def ticket_book (self, name, route, phone):
        if (len (self.buses) == 0):
            print ("No Bus Available")
            return
        
        route = route.lower()

        print ("----Available Buses----")
        for bus in self.buses:
            if bus.route == route:
                print (bus)

        number = input ("Enter The Number of Bus: ")
        bus = self.find_bus (number)

        if (bus is None):
            print ("No Bus Found")
            return

        bus.show_all_available_seats()
        
        
        print ("If Not Want to Book type -1")
        seat_number = int (input ("Enter Seat Number: "))
        if (seat_number == -1):
            print ("Select Another bus to book ticket")
            return
        seat_number-=1
        if seat_number < 0 or seat_number >= len(bus.seat):
            print("Invalid seat number.")
            return

        if bus.seat[seat_number] == "Booked":
            print(f"Seat Number {seat_number+1} is not available.")
            return

        bus.book_seat (seat_number)
        passenger = Passenger (name, phone, bus)
        self.add_passenger (passenger)
        print(f"Ticket booked successfully for {name}.")

    def show_passenger (self):
        if len(self.passengers) == 0:
            print ("No Booking yet")
            return

        print ("----Booked Passengers----")
        for p in self.passengers:
            print (p)