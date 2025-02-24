import matplotlib.pyplot as plt
import numpy as np

np.random.seed(2023)  # Semilla para replicar la aleatoriedad

def mc_Ac_aprox(N):
    plt.figure(figsize=(8, 8)) 
    x, y = np.random.uniform(0, 1, size=(2, N))

    interior = y <= x**2
    exterior = y <= 1

    Ac = (interior.sum() / (N) )  # Aproximación del área bajo la curva
    error = abs((Ac - 1/3) / (1/3)) * 100

    plt.plot(x[exterior], y[exterior], 'y.')
    plt.plot(x[interior], y[interior], 'k.')
    plt.title(f'Aproximación Monte Carlo del área bajo la curva con {N} puntos')
    plt.plot(0, 0, label='$\hat Ac$ = {:4.4f}\nerror = {:4.4f}%'
            .format(Ac,error), alpha=0)
    plt.legend(frameon=True, framealpha=0.9, fontsize=10)
    plt.axis('square')
    plt.show()

# Llamar a la función y mostrar el área y el error
mc_Ac_aprox(50000)
