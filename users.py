class User:
    def __init__ (self, name, email, phone, address) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    
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


class Restaurant:
    def __init__ (self, name):
        self.name = name
        self.employees = []  # like - database of employee
        
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











rest = Restaurant ("Mama Vagna Birani House")
ad = Admin ("Mozahid", "mim@gmail.com", 12345210, "Dhaka")
emp = Employee ("Sagor", "sagor@gmail.com", 13001110, "Khagan", 32, "Head Chef", 30000)


ad.add_employee (rest, emp)
ad.view_employee (rest)