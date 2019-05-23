import numpy as np
import matplotlib.pylab as plt
datos=np.genfromtxt("datoslp.dat")
t=datos[:,0]
y=datos[:,2]
x=datos[:,1]
plt.figure(figsize=[10,10])
plt.plot(x,y,c='deeppink')
plt.title("Desplazamiento particula")
plt.xlabel("desplazamiento en x")
plt.ylabel("desplazamiento en y")
plt.savefig("MartinValeria_final_15.pdf")