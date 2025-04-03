import Bodies
import nbodySystem 
import numpy as np 

class Runge_Kutta:
    def __init__(self, h, System):
        self.h = h 
        self.System = System 

    def simulate(self,num_steps):
        traj = [self.System.Bodies[i].q for i in range(0,self.System.n)]
        for j in range(0,num_steps):

            self.step()
            for i in range(0,self.System.n):
                traj[i] = np.vstack([traj[i],self.System.Bodies[i].q])

        return traj
            


    def step(self):
        p_1 = self.System.Bodies[0].q
        v_1 = self.System.Bodies[0].v
        for i in range(1,self.System.n):
            p_1 = np.append(p_1,self.System.Bodies[i].q)
            v_1 = np.append(v_1,self.System.Bodies[i].v)
        [k_1_v,k_1_a] = self.System.F(p_1,v_1)
        coeff = self.h/2
        [k_2_v,k_2_a] = self.System.F(p_1 + k_1_v * coeff , v_1 + k_1_a * coeff  )
        [k_3_v,k_3_a] = self.System.F(p_1 + k_2_v * coeff , v_1 + k_2_a * coeff  )
        [k_4_v,k_4_a] = self.System.F(p_1 + k_3_v * self.h , v_1 + k_3_a * self.h  )
        p_2 = p_1+ self.h/6 * (k_1_v+ 2*(k_2_v + k_3_v) + k_4_v)
        v_2 = v_1 + self.h/6 * (k_1_a+ 2*(k_2_a + k_3_a) + k_4_a)
        for i in range(0,self.System.n):
            self.System.Bodies[i].q = p_2[i*self.System.m : (i+1)*self.System.m]
            self.System.Bodies[i].v = v_2[i*self.System.m : (i+1)*self.System.m]