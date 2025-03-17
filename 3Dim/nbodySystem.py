
from Bodies import Body
import numpy as np 

class System:
    def __init__(self, Bodies, G = 6.67430 * 10**(-11), name = 'Some System'):
        ''' Bodies is an array whose entries are instances of the Body class '''
        self.Bodies = Bodies
        self.n = len(self.Bodies)
        self.m = len(self.Bodies[0].q)
        self.G = G
        self.name = name
        ''' The for-loop below checks if all the Bodies use the same coordinate-system '''
        for i in range(0, self.n ):
            error = ('Error: ' + self.name + ' contains Bodies in different dimensions. \n Coordinades of '
                 + self.Bodies[i].name + ' do not have the same dimension as the ones of ' 
                 + self.Bodies[0].name )
            assert self.m == len(self.Bodies[i].q), error
    
    def distMat(self):
        distMat = np.zeros((self.n,self.m))
        for i in range(0,self.n):
            for j in range(0,self.m):
                distMat[i,j] = self.Bodies[i].distance(self.Bodies[j])
        return distMat
    
    def forceMat(self):
        ''' Here we compute the force the Bodies generate amongst each-other '''
        Mat = np.zeros((self.n,self.m))
        for i in range(0,self.n):
            q = np.zeros(self.m)
            for j in range(0,self.m):
                
                if i==j:
                    q = q
                else:
                    q_1 =   np.subtract(self.Bodies[i].q,self.Bodies[j].q)
                    coeff = self.Bodies[i].m * self.Bodies[j].m / np.linalg.norm(q_1)**3
                    q = np.add(q,coeff*q_1)
            Mat[i,:] = q*self.G
        return Mat 




Test1 = Body(500, np.array([0,1,2]), np.array([4,5,6]), name = 'Body 1')
Test2 = Body(500, np.array([1,0,0]), np.array([4,5,6]))
Test3 = Body(500, np.array([0,0]), np.array([4,5,6]))
system = System([Test1,Test2,Test3])
print(system.forceMat())