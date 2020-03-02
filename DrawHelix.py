from vpython import *
import numpy as np
import time

n_periods = 10
n_points = 1000
thetas = np.linspace(0, 2*np.pi*n_periods, n_points)
spheres = []
for i in range(n_points):
    x = np.cos(thetas[i])
    y = np.sin(thetas[i])
    z = thetas[i]/10
    spheres.append(sphere(pos=vector(x, y, z), radius=0.1, color=color.cyan))

tic = time.time()
while True:
    t = time.time()-tic
    for i in range(n_points):
        spheres[i].pos.z = (2+np.sin(2*np.pi*t/2))*thetas[i]/10
