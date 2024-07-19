# Body2 represents the body directely orbiting the center in our the case the Sun resp Earth

import math


class Body2:
    def __init__(self,mass,dist_to_body1,radial_vlocity):
        self.mass = mass
        self.radius = dist_to_body1
        self.startingPosition =[dist_to_body1 , 0]
        self.v= radial_vlocity

    def pos_at_time(self,t):
        pos= [math.sin(self.v*t)*self.radius,  math.cos(self.v*t)*self.radius]
        return pos 
    



