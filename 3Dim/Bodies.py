''' This File contains the bodies for the considering  the n-dim Case'''
import math
import numpy as np

# Body1 represents the center of the system in our case the Sun or the earth

class Body:
    def __init__(self,mass,position, velocity, name = 'Some Body' ):
        self.m = mass
        self.q = position
        self.v = velocity
        self.state = np.append(self.q ,self.v)
        self.name = name 

    def distance(self,Body):
        ''' This method measures the distance from self to another instance of the body class '''
        dist = np.linalg.norm(np.subtract(self.q, Body.q))
        return dist




        
