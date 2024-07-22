from SpaceCraft import SpaceCraft
from Propulsion import Propulsion
from body1 import Body1
from body2 import Body2
import math
import matplotlib.pyplot as plt

# This class is used to simulate the system with earth, moon and space craft disregarding the sun.

class Three_Body_Sys:
    def __init__(self,body1, body2,SpaceCraft,initial_pos,initial_velocity):
        self.center  = body1
        self.moon = body2
        self.craft = SpaceCraft
        self.start = initial_pos
        self.v_0 = initial_pos+initial_velocity
        self.G =  G = 6.67430 * 10**(-11)

    def F(self,t,v):
        # below we define constants at time t. Note that v[0,1] is the position vector of the space craft and v[2,3] its velocity vector
        dist_sc_E = math.sqrt(v[0]**2 + v[1]**2)
        pos_M = self.moon.pos_at_time(t)
        dist_sc_M = math.sqrt((pos_M[0]-v[0])**2 + (pos_M[1]-v[1])**2)
        #below we compute the acceleration generated by the spacecrafts propulsion: [ a_Sc_1, a_Sc_2]
        Sc_const = self.craft.propulsion.delta_m * self.craft.propulsion.I  / (math.sqrt(v[2]**2 + v[3]**2)*self.craft.tim_mass(t))
        a_Sc_1 = v[2] * Sc_const
        a_Sc_2 = v[3] * Sc_const
        # below we compute the acceleration generated by the celestial bodies
        earth_const = self.G * self.center.mass / math.sqrt(v[0]**2 + v[1]**2)**3
        a_E_1 = -v[0] * earth_const
        a_E_2 = -v[1] * earth_const
        moon_const = self.G * self.moon.mass / dist_sc_M**3
        a_M_1 =  (pos_M[0]-v[0]) * moon_const
        a_M_2 =  (pos_M[1]-v[1]) * moon_const
        return [v[2], v[3] , a_Sc_1 + a_E_1 + a_M_1, a_Sc_2 + a_E_2 + a_M_2 ]
        

    # The below method simulates the orbit and returns a vector of points in the phase space that approximate the itenarary.
    def Runge_Kutta(self,h,t_max):
        t = range(0,t_max,h)
        n= len(t)
        sol = []
        sol.append(self.v_0)
    
        for i in range(n-1):
            k_1 = self.F(t[i],sol[i])
            k=0
            kk_2=[]
            for u in sol[i]:
                kk_2.append(u + [0.5*h*j for j in k_1][k] ) 
                k=k+1
            k_2 = self.F(t[i]+h/2, kk_2)
            k=0
            kk_3=[]
            for u in sol[i]:
                kk_3.append(u + [0.5*h*j for j in k_2][k] ) 
                k=k+1
            k_3 = self.F(t[i]+h/2, kk_3)
            k=0
            kk_4=[]
            for u in sol[i]:
                kk_4.append(u + [ 0.5*h*j for j in k_3][k] ) 
                k=k+1
            k_4 = self.F(t[i] + h ,kk_4)
            v_i=[]
            k=0
            for u in sol[i]:
                v_i.append( u + [h*j/6 for j in k_1][k] +  [2*j*h/6 for j in k_2][k] +  [2*j*h/6 for j in k_3][k]  + [h*j/6 for j in k_4][k])
                k = k+1
            sol.append(v_i)
        return sol 
     # this method plots an orbit (same as in Four_Body_System)
    
    def plot_orbit(self,h,t_max):
        sol = self.Runge_Kutta(h,t_max)
        x_values = []
        y_values = []
        for u in sol: 
            x_values.append(u[0])
            y_values.append(u[1])
        plt.plot(x_values,y_values)
        plt.show()


