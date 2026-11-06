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
        self.employees = []

    def add_employee (self, name, email, phone, address, age, designation, salary):
        employee = Employee (name, email, phone, address, age, designation, salary)
        self.employees.append (employee)
        print (f'{name} is added successfully')

    def view_employee (self):
        print ("-----Employee List-----")
        for emp in self.employees:
            print (emp.name, emp.email, emp.phone, emp.address, emp.designation, emp.salary)


# ad = Admin ("Mozahid", "mim@gmail.com", 12345210, "Dhaka")

# ad.add_employee ("Sagor", "sagor@gmail.com", 13001110, "Khagan", 32, "Head Chef", 30000)

# ad.view_employee ()