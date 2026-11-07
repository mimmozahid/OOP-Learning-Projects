
from abc import ABC
from order import Order

class User (ABC):
    def __init__ (self, name, email, phone, address) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address


class Customer (User):
    def __init__ (self, name, email, phone, address):
        super ().__init__ (name, email, phone, address)
        self.card = Order ()

    def view_menu (self, restuarant):
        restuarant.menu.show_menu (restuarant)

    def add_to_card (self, restuarant, item_name, quantity):
        item = restuarant.menu.find_item (item_name)

        if (item):
            if (quantity > item.quantity):
                print ("Item quantity exceeded")
            else:
                item.quantity = quantity
                self.card.add_item (item)
                print ("Item added")
        else:
            print ("Item Not Found")

    def view_card (self):
        print ("***** View Card *****")
        print ("Name\tPrice\tquantity")

        for item, quantity in self.card.items.items():
            print (f'{item.name} {item.price} {quantity}')
        
        print (f"Total Price: {self.card.total_price}")   

    def pay_bil (self):
        print (f'Total {self.card.total_price} paid successfully')
        self.card.clear()

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

    def view_menu (self, restaurant):
        restaurant.menu.show_menu()
        