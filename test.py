from SpaceCraft import SpaceCraft
from Propulsion import Propulsion
from body1 import Body1
from body2 import Body2
import math
import matplotlib.pyplot as plt
import vectors as vec

from TwoBodyOrbitalSystem import Two_Body_Sys

earth = Body1(5.9*10**24)

# setting parameters of the Engine and creating an instance of Propulsion class
name_prop = 'IonEngine'
spec_impuls = 19620
mass_throughput = 58 * 10**(-9)
mass_prop = 0.5
prop = Propulsion( name_prop ,  spec_impuls, mass_throughput, mass_prop)

# setting parameters of the Spacecraft and creating an instance of the SpaceCraft class
empty_weight = 6.5
fuel = 4.9
initial_position = [0,200000 + 6371000]
velocity = 7790 
craft = SpaceCraft(empty_weight, prop,fuel,initial_position, velocity)


initial_position = [0,200000 + 6371000]
initial_velocity = [7790,0]
system = Two_Body_Sys(earth,craft,initial_position,initial_velocity)

# plotting the orbit using the plot_orbit method.
t_max= 1000
h= 100
system.check(h,t_max)
