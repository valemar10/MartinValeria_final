import matplotlib.pylab as plt
import numpy as np
import random
v=1500
posicionesx=[4,10,12,80,50,40]
posicionesy=[100,5,80,50,50,200]
def velocidad(distancia, tiempo_promedio): #suponiendo torpedo muy superficial
	return(velocidad*tiempo)
def fun_verosimilitud(y_obser, y_modelo):
    chi = (1.0/2.0)*sum((y_obser-y_modelo)**2)
    return (np.exp(-(1/2)*chi))
print("El barco mas cercano es el barco 2, luego el barco, luego el barco 5, luego el barco 4 y finalmente el barco 3")

caminata_barco1enx=np.empty(0)
caminata_barco1enx=np.append(caminata_barco1enx, 4)
caminata_barco2enx=np.empty(0)
caminata_barco2enx=np.append(caminata_barco1enx, 10)
caminata_barco3enx=np.empty(0)
caminata_barco3enx=np.append(caminata_barco1enx, 12)
caminata_barco4enx=np.empty(0)
caminata_barco4enx=np.append(caminata_barco1enx, 80)
caminata_barco5enx=np.empty(0)
caminata_barco5enx=np.append(caminata_barco1enx, 50)
caminata_barco6enx=np.empty(0)
caminata_barco6enx=np.append(caminata_barco1enx, 40)
caminata_barco1eny=np.empty(0)
caminata_barco1eny=np.append(caminata_barco1enx, 100)
caminata_barco2eny=np.empty(0)
caminata_barco2eny=np.append(caminata_barco1enx, 5)
caminata_barco3eny=np.empty(0)
caminata_barco3eny=np.append(caminata_barco1enx, 80)
caminata_barco4eny=np.empty(0)
caminata_barco4eny=np.append(caminata_barco1enx, 50)
caminata_barco5eny=np.empty(0)
caminata_barco5eny=np.append(caminata_barco1enx,50)
caminata_barco6eny=np.empty(0)
caminata_barco6eny=np.append(caminata_barco1enx, 200)
verosimilitud=np.empty(0)

for i in range(1):
	b1x_nuevo = random.gauss(caminata_barco1enx[i], 3)
	b2x_nuevo = random.gauss(caminata_barco2enx[i], 3)
	b3x_nuevo = random.gauss(caminata_barco3enx[i], 3)
	b4x_nuevo = random.gauss(caminata_barco4enx[i], 3)
	b5x_nuevo = random.gauss(caminata_barco5enx[i], 3)
	b6x_nuevo = random.gauss(caminata_barco6enx[i], 3)
	b1y_nuevo = random.gauss(caminata_barco1eny[i], 3)
	b2y_nuevo = random.gauss(caminata_barco2eny[i], 3)
	b3y_nuevo = random.gauss(caminata_barco3eny[i], 3)
	b4y_nuevo = random.gauss(caminata_barco4eny[i], 3)
	b5y_nuevo = random.gauss(caminata_barco5eny[i], 3)
	b6y_nuevo = random.gauss(caminata_barco6eny[i], 3)
	