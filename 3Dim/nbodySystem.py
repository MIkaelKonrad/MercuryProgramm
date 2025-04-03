# python nbodySystem.py
from Bodies import Body
import numpy as np 
import euler

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
                    coeff = (-1)*self.Bodies[i].m * self.Bodies[j].m / np.linalg.norm(q_1)**3
                    q = np.add(q,coeff*q_1)
            Mat[i,:] = q*self.G
        return Mat 



if  __name__ == '__main__': 

    Test1 = Body(5000000000000, np.array([0,0,0]), np.array([0,0,0.1]), name = 'Body 1')
    Test2 = Body(1000, np.array([37,40,35]), np.array([0,0.5,0]))
    Test3 = Body(1000, np.array([-25,-15,-48]), np.array([-0.5,0,0]))
    system = System([Test1,Test2,Test3])
    sol  = euler.Euler( 10, system )
    num_steps = 60
    traj = sol.simulate(num_steps)
    print(traj)


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
    ax.set(xlim3d=(-200, 200), xlabel='X')
    ax.set(ylim3d=(-200, 200), ylabel='Y')
    ax.set(zlim3d=(-200, 200), zlabel='Z')

    # Creating the Animation object
    ani = animation.FuncAnimation(
    fig, update_lines, num_steps, fargs=(traj, lines), interval=100)

    plt.show()

   