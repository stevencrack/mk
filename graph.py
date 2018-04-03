import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("datos.txt")
plt.figure()
x=np.linspace(0,160,160)
plt.plot(data[:,0], data[:,1])
plt.show()
plt.savefig("graph_album.png")

