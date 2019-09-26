class Vehicle():

    def __init__(self, num_wheels, capacity, colour, year):
        self.num_wheels = num_wheels
        self.capacity = capacity
        self.colour = colour
        self.year = year

    def accelerate(self):
        return 'VROOOOOOOM NEEEEOOOOWW'

    def brake(self):
        return 'ESSKEEEEEEEEET'

    def turn(self, direction):
        return 'WEEEEEEEEE! *turning ' + direction + '*'    
    
    def play_sound(self):
        return 'VrOoOoOoOoOMMM'

