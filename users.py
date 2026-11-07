class User:
    def __init__ (self, name, email, phone, address) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address


class Customer (User):
    def __init__ (self, name, email, phone, address):
        super ().__init__ (name, email, phone, address)
        self.card = None

    def view_menu (self, restuarant):
        restuarant.menu.show_menu ()

    def add_to_card (self, restuarant, item_name):
        item = restuarant.menu.find_item (item_name)

        if (item):
            pass
        else:
            print ("Item Not Found")

    def view_card (self):
        print ("***** View Card *****")
        print ("Name\tPrice\tquantity")
        

    
class Employee (User):
    def __init__ (self, name, email, phone, address, age, designation, salary):
        super().__init__ (name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin (User):
    def __init__ (self, name, email, phone, address):
        super ().__init__ (name, email, phone, address)

    def add_employee (self, restaurant, employee):
        restaurant.add_employee (employee)

    def view_employee (self, restaurant):
        restaurant.view_employee ()

    def add_new_item (self, restaurant, item):
        restaurant.menu.add_menu_item (item)

    def remove_item (self, restaurant, item):
        restaurant.menu.remove_item (item)

class Restaurant:
    def __init__ (self, name):
        self.name = name
        self.employees = []  # like - database of employee
        self.menu = FoodItem ()


    def add_employee (self, employee):
        self.employees.append (employee)

    def view_employee (self):
        print ("-----Employee List-----")
        for emp in self.employees:
            print (emp.name, emp.email, emp.phone, emp.address, emp.designation, emp.salary)


class Menu:
    def __init__ (self):
        self.items = []   # like - database of employee

    def add_menu_item (self, item):
        self.items.append (item)

    def find_item (self, item_name):
        for item in self.items:
            if (item.name.lower() == item_name.lower()):
                return item
        return None

    def remove_item (self, item_name):
        item = self.find_item (item_name)
        
        if (item):
            self.items.remove (item)
            print ("Remove successfully")
        else:
            print ("Item not found")

    def show_menu (self):
        print ("***** Menu ******")
        print ("Name\tprice\tquantity")
        for item in self.items:
            print (f'{item.name}\t{item.price}\t{item.quantity}')
        


class FoodItem:
    def __init__ (self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity









rest = Restaurant ("Mama Vagna Birani House")
ad = Admin ("Mozahid", "mim@gmail.com", 12345210, "Dhaka")
emp = Employee ("Sagor", "sagor@gmail.com", 13001110, "Khagan", 32, "Head Chef", 30000)

mn = Menu ()
item1 = FoodItem ("Pizza", 300, 11)
item2 = FoodItem ("Burger", 130, 7)
mn.add_menu_item (item1)
mn.add_menu_item (item2)
mn.show_menu ()

# ad.add_employee (rest, emp)
# ad.view_employee (rest)