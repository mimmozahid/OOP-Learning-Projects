from bus import*

class Passenger:
    def __init__ (self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus #* bus = Object

    def __str__(self):
        return (f"Passenger: {self.name} | Phone: {self.phone}\nBus: {self.bus.number} ({self.bus.route})\n")
