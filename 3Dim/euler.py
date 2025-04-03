import Bodies
import nbodySystem 
import numpy as np 

class Euler:
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
        Mat = self.System.forceMat()
        for i in range(0,self.System.n):
            self.System.Bodies[i].q = self.System.Bodies[i].q + self.h * self.System.Bodies[i].v
            self.System.Bodies[i].v = self.System.Bodies[i].v + self.h * Mat[i]/self.System.Bodies[i].m
