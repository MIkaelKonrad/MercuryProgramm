import Bodies
import nbodySystem 
import numpy as np 

class Euler:
    def __init__(self, h, System):
        self.h = h 
        self.System = System 

    def simulate(self,n):
        for j in range(0,n):
            print('\n Step '+ str(j) + ' : '+ str(self.System.Bodies[0].q ))
            self.step()
            
    
    def step(self):
        Mat = self.System.forceMat()
        for i in range(0,self.System.n):
            self.System.Bodies[i].q = self.System.Bodies[i].q + self.h * self.System.Bodies[i].v
            self.System.Bodies[i].v = self.System.Bodies[i].v + self.h * Mat[i]
