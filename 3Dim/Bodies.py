''' This File contains the bodies for the considering  the 3dim Case'''
import math
import numpy as np

# Body1 represents the center of the system in our case the Sun or the earth

class Body:
    def __init__(self,mass,position, velocity ):
        self.m = mass
        self.q = position
        self.v = velocity
        self.state = np.append(self.q ,self.v)

    def distance(self,Body):
        '''dist = 0
        for i in range(0,len(self.q)):
            dist = dist + (self.q[i]-Body.q[i])**2
        dist = math.sqrt(dist)'''
        dist = np.linalg.norm(np.subtract(self.q, Body.q))
        return dist




Test1 = Body(500, np.array([0,1,2]), np.array([4,5,6]))
Test2 = Body(500, np.array([1,0,0]), np.array([4,5,6]))
print(Test1.distance(Test2))

        
