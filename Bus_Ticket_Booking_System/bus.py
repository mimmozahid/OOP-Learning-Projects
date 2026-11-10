class Bus:
    def __init__ (self, number, route, total_seat):
        self.number = number
        self.route = route
        self.total_seat = total_seat
        self.seat = ["Empty"] * total_seat
        self.booked_seat = 0 #! have to work


    def available_seats(self):
        return self.total_seat - self.booked_seat

    def show_all_available_seats (self):
        for i, st in enumerate(self.seat):
            print (f"Seat Number {i}: {st}")

    def book_seat (self, idx):
        if self.seat[idx] == "Empty":
            self.seat[idx] = "Booked"
            self.booked_seat += 1
            print ("Seat Number {idx} is Booked Successfully.")
        else:
            print ("Seat Number {idx} is is not available.")

    def __str__(self):
        return (f"Bus No: {self.number} | Route: {self.route}\nAvailable Seats: {self.available_seats()} {self.total_seat}")