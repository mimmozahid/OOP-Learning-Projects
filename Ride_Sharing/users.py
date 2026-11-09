from abc import ABC, abstractmethod

class User (ABC):
    def __init__ (self, name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0
        
    
    @abstractmethod
    def display_profile (self):
        raise NotImplementedError


class Rider (User):
    def __init__ (self, name, email, nid, current_location, initial_amount) -> None:
        super ().__init__ (name, email, nid)
        self.current_ride = None
        self.current_location = current_location
        self.wallet = initial_amount

    def display_profile (self):
        print (f'Rider: {self.name} and Email: {self.email}.')

    def load_cash (self, amount):
        if amount > 0:
            self.wallet += amount
        else:
            print ("Amount less than 0")

    def update_location (self, current_location):
        self.current_location = current_location

    def request_ride (self, ride_sharing, destination, vehicle_type):
        pass

    def show_current_ride (self):
        print ("Ride Details")
        print (f"Rider: {self.name}")
        print (f"Driver: {self.current_ride.driver.name}")
        # print (f"Selected Car: {}")




class Driver (User):
    def __init__ (self, name, email, nid, current_location):
        super().__init__ (name, email, nid)
        self.current_location = current_location
        self.wallet = 0

    def display_profile (self):
        print (f"Driver Name: {self.name}")

    def except_ride (self, ride):
        ride.start_ride ()
        ride.set_driver (self)

    def reach_destination (self, ride):
        ride.end_ride ()