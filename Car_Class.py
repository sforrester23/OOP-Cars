from Vehicle_Class import *

class Car(Vehicle):
    def __init__(self, num_wheels, capacity, colour, year, brand, model, license_plate, airbag = True):
        super().__init__(num_wheels, capacity, colour, year)
        self.brand = brand
        self.model = model
        self.license_plate = license_plate
        self.airbag = airbag

    def play_music(self, volume):
        return 'MMSSST MMMMSSST MMMSSSST at {}% volume'.format(volume)

    def horn(self):
        return 'HOOOOOOOONNNNKKKKKK'

    def lock_it(self):
        return 'CHUH CHUH'

    def windshield_wipe(self):
        return 'WHOOSH WHOOSH WHOOSH'

    def crash(self, object):
        return 'BANG WOLLOP DING. Hit a {}'.format(object)
    
    def play_sound(self):
        return 'VROOOOOMMMMM'
    
    # Car will inherit all the functions from the Vehicle class
    