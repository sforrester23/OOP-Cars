from Vehicle_Class import *
from Car_Class import *
from Bicycle_Class import *
from Car_Class_2 import *
#
# vehicle_1 = Vehicle(4, 5, 'Blue', 1989)
#
# car_1 = Car(4, 5, 'Grey', 2019, 'Hyundai', 'i30', 'GY59 GYK', True)
#
# print(car_1.license_plate)
# print("Wow! That's a super nice {} {} {} {} with {} doors and {} person capacity.".format(car_1.colour, car_1.year, car_1.brand, car_1.model, car_1.num_wheels, car_1.capacity))
#
# bicycle_1 = Bicycle(2, 1, 'Midnight Grey', 2001, 'normal', 21, True)
#
# if bicycle_1.basket == False:
#     print('That is a lovely {} {} bicycle with {} handlebars and {} gears but no basket'.format(bicycle_1.colour, bicycle_1.year, bicycle_1.handle_bar, bicycle_1.gears, bicycle_1.basket))
# else:
#     print('That is a lovely {} {} bicycle with {} handlebars and {} gears and a basket.'.format(bicycle_1.colour, bicycle_1.year, bicycle_1.handle_bar, bicycle_1.gears, bicycle_1.basket))


car_example = Car2(4,5,'green', 'Volvo', 'XC90', 'XOXOX')
# print('Proof of inheritance:')
# print(car_example)
# print(car_example.make_sound()) # Inheriting the same methods as Vehicle class is INHERITANCE
#
# print('/////////////////////////////////')
#
# vehicle_example = Vehicle2(2,4, 'Blue')
# print('Proof of method polymorphism with make_sound():')
# print(vehicle_example.make_sound())
# print(car_example.make_sound()) # METHOD POLYMORPHISM displayed by the same method being called on a parent class and its sub class but being different because it is defined wrong
#


print('Playing with Encapsulation')
print(car_example.wheels)
print(car_example._accidents)
# print(car_example.__miles) # This will break, because it is a private/encapsulated figure

print(car_example.set_miles(105))
print(car_example.show_miles())