from ride import*
from users import*
from vehicle import*


pathao = RideSharing ("Pathao")

rider_01 = Rider ("Mozahid", "mzhd@gmail.com", 13455, "Ashulia", 5090)
pathao.add_rider (rider_01)

driver_01 = Driver ("Karim", "karim@gmail.com", 12344, "Savar")
pathao.add_driver (driver_01)

rider_01.request_ride (pathao, "Rajshahi", 'car')
driver_01.reach_destination (rider_01.current_ride)
rider_01.show_current_ride()

print (pathao)