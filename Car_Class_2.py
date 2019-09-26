from Vehicle_Class_2 import *

class Car2(Vehicle2):
    def __init__(self, wheels, capacity, colour):
        super().__init__(wheels, capacity, colour, make, model, plate)
        self.make = make
        self.model = model
        self.plate = plate


    def make_sound(self):
        return 'REVVREVVVREVVV'

    def play_music(self, song):
        return 'PLAY: ' + song
    
