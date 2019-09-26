from Vehicle_Class_2 import *

class Car2(Vehicle2):
    def __init__(self, wheels, capacity, colour,  make, model, plate):
        super().__init__(wheels, capacity, colour)
        self.make = make
        self.model = model
        self.plate = plate
        self._accidents = 0 # Visibility is limited
        self.__miles = 1000000 # Visibility and Access is restricted


    def make_sound(self):
        return 'REVVREVVVREVVV'

    def play_music(self, song):
        return 'PLAY: ' + song
    
    def show_miles(self):
        return self.__miles

    def set_miles(self, miles):
        self.__miles = miles
        return 'miles set to {} miles'.format(miles)
    
