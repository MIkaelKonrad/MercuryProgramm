# when simulating both the earth and the suns effect the moon will represented by an instance of body3

from body2 import Body2
import math


class Body3:
    def __init__(self,mass,dist_to_body2,radial_vlocity,body2):
        self.mass = mass
        self.radius = dist_to_body2
        self.startingPosition =[dist_to_body2 + body2.radius , 0]
        self.v= radial_vlocity
        self.body2 = body2

    def pos_at_time(self,t):
        pos_body2 = self.body2.pos_at_time(t)
        pos= [pos_body2[0]+math.sin(self.v*t)*self.radius,  pos_body2[1]+math.cos(self.v*t)*self.radius]
        return pos 
    