#The below class contains parameters of a Space craft.

import Propulsion


class SpaceCraft:
    def __init__(self, mass, propulsion,fuel,initial_position, initial_velocity):
        self.empty_weight = mass + propulsion.mass
        self.starting_weight = mass + propulsion.mass + fuel 
        self.propulsion = propulsion
        self.in_pos = initial_position 
        self.in_vel = initial_velocity
    
    def tim_mass(self, t):
        t_mass = self.starting_weight - self.propulsion.delta_m * t
        if t_mass > self.empty_weight :
            return t_mass
        else:
            print('out of fuel')
            return self.empty_weight

    
    



