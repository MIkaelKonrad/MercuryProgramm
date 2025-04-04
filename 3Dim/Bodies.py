# python Bodies.py

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
        self.propelled = False

    def distance(self,Body):
        ''' This method measures the distance from self to another instance of the body class '''
        dist = np.linalg.norm(np.subtract(self.q, Body.q))
        return dist

class Propulsion:
    def __init__(self, name, spec_impuls, mass_throughput, mass):
        self.name = name
        self.I = spec_impuls
        self.delta_m = mass_throughput
        self.mass = mass


class PropBody(Body):
    def __init__(self,payload,position, velocity, propulsion, name = 'Some propelled Body' ):
        super().__init__(payload + propulsion.mass ,position, velocity)
        self.prop = propulsion
        self.name = name
        self.payload = payload
        self.fueld = True
        self.propelled = True

    def update_mass(self,t):
        if self.payload < self.mass:
            self.mass = self.mass - t*self.prop.delta_m
        else:
            self.fueled = False

        
if  __name__ == '__main__': 
    Test4 = Body(10000000, np.array([12,0,50]), np.array([0,0,0]))

    name_prop = 'IonEngine'
    spec_impuls = 19620
    mass_throughput = 58 * 10**(-9)
    mass_prop = 0.5
    prop = Propulsion( name_prop ,  spec_impuls, mass_throughput, mass_prop)


    Test5 = PropBody(10000000, np.array([-50,-15,-30]), np.array([0,0,0]),prop)
    print(Test5.propelled)
