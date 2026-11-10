from bus import*
from bus_system import*

    
mm = BusSystem ("MM Travels")

def admin_panel ():
    username = input ("Enter username: ")
    password = input ("Enter password: ")

    while 1:
        if not (mm.admin_login (username, password)):
            print ("Wrong username or password")
            break

        print ("----Welcome Admin----")
        print ("1. Add Bus")
        print ("2. View All Buses")
        print ("3. View Booked Passengers")
        print ("4. Exit")

        choice = input ("Enter Your Choice: ")

        if (choice == '1'):
            bus_number = input ("Enter Bus Number: ")
            route = (input ("Enter Bus Route: ")).lower()
            total_seat = int (input ("Enter Total Seats: "))

            mm.add_bus (bus_number, route, total_seat)
        
        elif choice == '2':
            mm.show_buses ()
        elif choice == '3':
            mm.show_passenger ()
        elif choice == '4':
            mm.logout()
            break
        else:
            print ("Invalid Choice. Try again...")


def book_ticket ():
    name = input ("Enter Your Name: ")
    phone = input ("Enter Your Phone Number: ")
    route = input ("Enter Your Route: ")

    print (f"----Welcome {name}----")

    while 1:
        print ("1. Ticket Book")
        print ("2. Exit")

        choice = input ("Enter Your Choice: ")
        
        if (choice == '1'):
            mm.ticket_book (name, route, phone)

        elif choice == '2':
            break

        else:
            print ("Invalid Choice, Try again...")
    


while 1:
    print ("\t---Welcom---")
    print ("Bus Ticket Booking System")
    print ("1. Admin Login")
    print ("2. Book Ticket")
    print ("3. View Buses")
    print ("4. Exit")

    choice = input ("Enter Your Choice: ")
    if choice == '1':
        admin_panel ()

    elif choice == '2':
        book_ticket ()
    
    elif choice == '3':
        mm.show_buses ()
    
    elif choice == '4':
        print ("Thanks for using this system")
        break
    else:
        print ("Invalid Choice, Try again...")
