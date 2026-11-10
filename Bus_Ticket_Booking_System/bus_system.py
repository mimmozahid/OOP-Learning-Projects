from bus import*
from passenger import*

class BusSystem:
    def __init__ (self, company_name):
        self.company_name = company_name
        self.buses = []
        self.passengers = []
        self.admin = Admin ("admin", "@123")
        self.login_admin = False
    
    def add_bus (self, number, route, seats):
        bus = Bus (number, route, total_seat)
            

    def add_passenger (self, passenger):
        self.passengers.append (passenger)

    def find_bus (self, number):
        for bus in self.buses:
            if bus.number == number:
                return
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
        
        print ("----Available Buses----")
        for bus in self.buses:
            if bus.route == route:
                print (bus)

        number = input ("Enter The Number of Bus: ")
        bus = self.find_bus (number)
        bus.show_all_available_seats()
        seat_number = int (input ("Enter Seat Number: "))
        bus.book_seat (seat_number)
        Passenger (name, phone, bus)
        self.add_passenger (Passenger)

    