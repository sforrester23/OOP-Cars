from Vehicle_Class import *
from Car_Class import *
from Bicycle_Class import *

vehicle_1 = Vehicle(4, 5, 'Blue', 1989)

car_1 = Car(4, 5, 'Grey', 2019, 'Hyundai', 'i30', 'GY59 GYK', True)

print(car_1.license_plate)
print("Wow! That's a super nice {} {} {} {} with {} doors and {} person capacity.".format(car_1.colour, car_1.year, car_1.brand, car_1.model, car_1.num_wheels, car_1.capacity))

bicycle_1 = Bicycle(2, 1, 'Midnight Grey', 2001, 'normal', 21, True)

if bicycle_1.basket == False:
    print('That is a lovely {} {} bicycle with {} handlebars and {} gears but no basket'.format(bicycle_1.colour, bicycle_1.year, bicycle_1.handle_bar, bicycle_1.gears, bicycle_1.basket))
else:
    print('That is a lovely {} {} bicycle with {} handlebars and {} gears and a basket.'.format(bicycle_1.colour, bicycle_1.year, bicycle_1.handle_bar, bicycle_1.gears, bicycle_1.basket))

