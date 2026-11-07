from food_item import FoodItem
from menu import Menu
from order import Order
from restaurant import Restaurant
from users import User, Customer, Employee, Admin

restaurant = Restaurant ("Kacchi Bhai")

def customer_menu ():
    name = input ("Enter Your Name: ")
    phone = int (input ("Enter Your Phone Number: "))
    email = input ("Enter Your Email: ")
    address = input ("Enter Your Address: ")
    customer = Customer (name, email, phone, address)

    while True:
        print (f'-------Welcome {customer.name}------')
        print ("1. View Menu")
        print ("2. Add Item to Card")
        print ("3. View Card")
        print ("4. Pay Bill")
        print ("5. Exit")

        choice = int (input ("Enter Your Choice: "))

        if (choice == 1):
            customer.view_menu (restuarant=restaurant)
        
        elif (choice == 2):
            item_name = input ("Enter Item Name: ")
            item_quantity = int (input ("Enter Item Quantity: "))

            customer.add_to_card (restuarant=restaurant, item_name=item_name, quantity=item_quantity)
        
        elif choice == 3:
            customer.view_card ()

        elif choice == 4:
            customer.pay_bil ()

        elif choice == 5:
            break
        else:
            print ("Invalid Choice")
        
def admin_menu ():
    name = input ("Enter Your Name: ")
    phone = input ("Enter Your Phone Number: ")
    email = input ("Enter Your Email: ")
    address = input ("Enter Your Address: ")
    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print (f'-------Welcome Admin------')
        print ("1. Add New Item")
        print ("2. Add New Employee")
        print ("3. View Employee")
        print ("4. View Items")
        print ("5. Delete Item")
        print ("6. Exit")

        choice = int (input ("Enter Your Choice: "))

        if (choice == 1):
            item_name = input ("Enter Item Name: ")
            item_price = int (input ("Enter Item Price: "))
            item_quantity = int (input ("Enter Item quantity: "))
            item = FoodItem (name=item_name, price=item_price, quantity=item_quantity)
            admin.add_new_item (restaurant, item)
        
        elif (choice == 2):
            name = input ("Enter Employee Name: ")
            email = input ("Enter Employee Email: ")
            phone = input ("Enter Employee Phone Number: ")
            address = input ("Enter Employee Address: ")
            age = input ("Enter Employee Age: ")
            designation = input ("Enter Employee Designation: ")
            salary = input ("Enter Employee Salary: ")

            employee = Employee (name=name, email=email, phone=phone, address=address, age=age, designation=designation, salary=salary)
            admin.add_employee (restaurant=restaurant, employee=employee)

        elif choice == 3:
            admin.view_employee (restaurant=restaurant)

        elif choice == 4:
            admin.view_menu (restaurant=restaurant)

        elif choice == 5:
            remove_item_name = input ("Enter Item Name: ")
            admin.remove_item (restaurant=restaurant, item=remove_item_name)
            
        elif choice == 6:
            break
        
        else:
            print ("Invaid Choice :)")


while True:
    print ("******Welcome********")
    print ("1. Customer")
    print ("2. Admin")
    print ("3. Exit")

    choice = input ("Enter Your Choice: ")

    if (choice == '1'):
        customer_menu ()

    elif choice == '2':
        admin_menu ()

    elif choice == '3':
        break
    
    else:
        print ("Invalid Choice")
