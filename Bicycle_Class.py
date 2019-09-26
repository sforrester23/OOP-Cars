from Vehicle_Class import *

class Bicycle(Vehicle):
    def __init__(self, num_wheels, capacity, colour, year, handle_bar = 'normal', gears = 18, basket = False):
        super().__init__(num_wheels, capacity, colour, year)
        self.handle_bar = handle_bar
        self.gears = gears
        self.basket = basket

    def peddle(self, effort = 3):
        if effort >5:
            return 'GRUNT GRUNT GRUNT'
        else:
            return 'PUFF PUFF PUFF'

    def wheely(self):
        return 'YEEEEET'

    def chain_it(self):
        return '*FIDDLE* *FIDDLE*'

    def play_sound(self):
        return 'BRING BRING BRING BRING'
    # Bicycle will inherit all the standard functions from vehicle but the 'play_sound' function has been changed for the bike. This is an example of polymorphism.

