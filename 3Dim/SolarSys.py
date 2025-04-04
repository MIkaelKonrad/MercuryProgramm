# python SolarSys.py

import Bodies as Bd
import nbodySystem as nS
import RungeKutta
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation

Earth = Bd.Body(5.972*10**24,np.array([0,1.47*10**11,0]) , np.array([30290,0,0]) , name = 'Earth')
Sun = Bd.Body(1.989*10**30, np.array([0,0,0]), np.array([0,0,0]), name = 'Sun')
Venus = Bd.Body(4.867*10**24, np.array([0,-1.075*10**11,0]), np.array([35500,0,0]), name = 'Venus')
Mars = Bd.Body(0.64188*10**24, np.array([2.06*10**11,0,0]), np.array([0,26500,0]), name = 'Mars ')
Mercury = Bd.Body(0.33*10**24 , np.array([-0.46*10**11,0,0]), np.array([0,59000,0]), name = 'Mercury')

if  __name__ == '__main__': 
    
    
    system = nS.System([Earth, Sun, Venus , Mars, Mercury ])
    sol  = RungeKutta.Runge_Kutta(10000,system)
    num_steps = 3000
    traj = sol.simulate(num_steps)

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
    print(np.add([1,2,3],1))
    plt.show()

   