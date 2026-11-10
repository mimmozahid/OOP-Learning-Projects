from bus_system import*

class Admin:
    def __init__ (self, username, password):
        self.__username = username
        self.__password = password

    def logIn (self, uName, pWord) -> bool:
        return self.__username == uName and self.__password == pWord