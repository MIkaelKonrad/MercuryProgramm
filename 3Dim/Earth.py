# python Earth.py

import Bodies as Bd
import nbodySystem as nS
import RungeKutta
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation

Earth = Bd.Body(5.972*10**24,np.array([0,0,0]) , np.array([0,0,0]) , name = 'Earth')
Moon = Bd.Body(7.34767309*10**22,  np.array([0,3.63104*10**8,0]), np.array([1070,0,0]), name = 'Moon')

if  __name__ == '__main__': 
    #np.array([0,1.47*10**11,0]) 
    system = nS.System([Earth, Moon ])
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
    ax.set(xlim3d=(-4*10**8, 4*10**8), xlabel='X')
    ax.set(ylim3d=(-4*10**8, 4*10**8), ylabel='Y')
    ax.set(zlim3d=(-4*10**8, 4*10**8), zlabel='Z')

    # Creating the Animation object
    ani = animation.FuncAnimation(
    fig, update_lines, num_steps, fargs=(traj, lines), interval=5)
    
    plt.show()

   