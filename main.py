from SpaceCraft import SpaceCraft
from Propulsion import Propulsion
from body1 import Body1
from body2 import Body2
from body3 import Body3
import numpy as np
import math
import matplotlib.pyplot as plt
from ThreeBodyOrbitalSystem import Three_Body_Sys
from FourBodyOrbitalSystem import Four_Body_Sys

# defining the celestial bodies as instances of Body classes from the body.py files
earth = Body2(5.9*10**24,149*10**9,2*math.pi/(365*24*3600))
moon = Body3(0.07346*10**24,384400000, 2.7 * 10 **(-6), earth )
sun = Body1(1.98892*10**30)


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

# setting up the system by creating an instance of .._Body_Sys class
initial_velocity = [7790,0]
system = Four_Body_Sys(sun,earth,moon,craft,initial_position,initial_velocity)

# plotting the orbit using the plot_orbit method.
t_max= 64000000
h= 100
system.plot_orbit(h,t_max)