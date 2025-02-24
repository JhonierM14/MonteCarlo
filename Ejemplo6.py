import numpy as np

np.random.seed(2023)  # Semilla para replicar la aleatoriedad

def vl_esfera_aprox(N):
    x, y = np.random.uniform(-1, 1, size=(2, N))
    z, w = np.random.uniform(-1, 1, size=(2, N))
    volumenCuadrado = pow(2, 4)
    interior = (x**2 + y**2 + z**2 + w**2) <= 1 # condicion
    volumenEsfera = ( interior.sum() * volumenCuadrado / (N) )  # Aproximación volumen
    error = abs(np.pi**2 /2 - volumenEsfera) / (np.pi**2 /2) * 100
    print("Volumen calculado: ", volumenEsfera)
    print("Volumen real: ", np.pi**2 /2, "Error: ", error)

vl_esfera_aprox(50000)
