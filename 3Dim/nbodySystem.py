# python nbodySystem.py
from Bodies import Body
import numpy as np 
import euler
import RungeKutta
import math

# used for creating the visualization
import matplotlib.pyplot as plt
import matplotlib.animation as animation


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
    ''' Creates the function defining the dyn sys at the moment this function is not yet time depend however 
    when we add propelled bodies it will become time dependent due to fuel usage  ''' 
    def F(self,p,v,t):
            if self.m * self.n != len(p):
                print('Error dimensions do not add up!')
            else: 
                '''calculating the distances between the bodies '''
                distMat = np.zeros((self.n,self.n))
                for i in range(0,self.n):

                    for j in range(0,self.n):
                        distMat[i,j] = math.sqrt(np.sum( np.square(p[i*self.m :(i+1)*self.m ] - p[j*self.m:(j+1)*self.m])))
                
                ''' calculating the acceleration experienced by each body '''
                accVec = np.zeros(self.n*self.m) 
                for i in range(0,self.n):
                    if self.Bodies[i].propelled == True:
                        if self.Bodies[i].fueled == True:
                           # add the acceleration the propulsion provides here
                           q  = np.zeros(self.m)
                        else: 
                            q  = np.zeros(self.m)
                    else:
                        q = np.zeros(self.m)
                    
                    for j in range(0,self.n):
                        if i==j:
                            q = q
                        else:
                            q_1 =  distMat[i,j]
                            coeff = (-1)*self.Bodies[j].m / q_1**(3)
                            q = q+ coeff*(p[i*self.m :(i+1)*self.m ] - p[j*self.m:(j+1)*self.m])
                    accVec[i*self.m : (i+1)*self.m] =  q *self.G

                return [v, accVec]



    def distMat(self):
        distMat = np.zeros((self.n,self.m))
        for i in range(0,self.n):
            for j in range(0,self.n):
                distMat[i,j] = self.Bodies[i].distance(self.Bodies[j])
        return distMat
    
    def accMat(self):
        ''' Here we compute the force the Bodies generate amongst each-other '''
        Mat = np.zeros((self.n,self.m))
        for i in range(0,self.n):
            q = np.zeros(self.m)
            for j in range(0,self.n):
                
                if i==j:
                    q = q
                else:
                    q_1 =   np.subtract(self.Bodies[i].q,self.Bodies[j].q)
                    coeff = (-1)*self.Bodies[i].m * self.Bodies[j].m / np.linalg.norm(q_1)**3
                    q = np.add(q,coeff*q_1)
            Mat[i,:] = q*self.G/self.Bodies[i].m
        return Mat 



if  __name__ == '__main__': 
    #np.array([0,1.47*10**11,0]) 
    Earth = Body(5.972*10**24,np.array([0,1.47*10**11,0]) , np.array([30290,0,0]) , name = 'Earth')
    Moon = Body(7.34767309*10**22, np.array([0,1.47*10**11,0]) - np.array([0,3.63104*10**8,0]), np.array([30290,0,0]) - np.array([1070,0,0]), name = 'Moon')
    Sun = Body(1.989*10**30, np.array([0,0,0]), np.array([0,0,0]), name = 'Sun')
    Venus = Body(4.867*10**24, np.array([0,-1.075*10**11,0]), np.array([35500,0,0]), name = 'Venus')
    Mars = Body(0.64188*10**24, np.array([2.06*10**11,0,0]), np.array([0,26500,0]), name = 'Mars ')
    Mercury = Body(0.33*10**24 , np.array([-0.46*10**11,0,0]), np.array([0,59000,0]), name = 'Mercury')
    system = System([Earth, Sun, Venus , Mars, Mercury ])
    sol  = RungeKutta.Runge_Kutta(10000,system)
    num_steps = 3000
    traj = sol.simulate(num_steps)
    #print(traj)


    def update_lines(num, traj, lines):
        for line, walk in zip(lines, traj):
            line.set_data_3d(walk[:num, :].T)
        return lines


    # Attaching 3D axis to the figure
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    # Create lines initially without data
    lines = [ax.plot([], [], [])[0] for _ in traj]

    # Setting the Axes properties
    ax.set(xlim3d=(-2.6*10**11, 2.6*10**11), xlabel='X')
    ax.set(ylim3d=(-2.6*10**11, 2.6*10**11), ylabel='Y')
    ax.set(zlim3d=(-2.6*10**11, 2.6*10**11), zlabel='Z')

    # Creating the Animation object
    ani = animation.FuncAnimation(
    fig, update_lines, num_steps, fargs=(traj, lines), interval=5)

    plt.show()

   