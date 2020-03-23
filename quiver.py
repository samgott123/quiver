import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation


fig , ax = plt.subplots()

X = np.arange(-10,10,2)
Y = np.arange(-10,10,2)

x,y = np.meshgrid(X,Y)
U =np.ones(x.size)
V= y

																																																																



q = ax.quiver(x,y,U,V)
ax.set_aspect('equal')

plt.show()


