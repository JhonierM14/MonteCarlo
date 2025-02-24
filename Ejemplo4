import matplotlib.pyplot as plt
import numpy as np

np.random.seed(2023)  # Semilla para replicar la aleatoriedad

def mc_pi_aprox(N):
    eje_x = 2; eje_y = 1
    plt.figure(figsize=(8, 8)) 
    x, y = np.random.uniform(0, 4, size=(2, N))

    interior = ( (x - 2)**2/eje_x**2 + (y - 2)**2/eje_y**2 ) <= 1
    exterior = y <= 4
    
    pi = ( (16 * interior.sum()) / (N) )  # Aproximación de pi
    error = abs((pi - np.pi) / (np.pi)) * 100

    plt.plot(x[exterior], y[exterior], 'y.')
    plt.plot(x[interior], y[interior], 'k.')
    plt.title(f'Aproximación Monte Carlo del valor de pi con {N} puntos')
    plt.plot(0, 0, label='$\hat pi$ = {:4.4f}\nerror = {:4.4f}%'
            .format(pi, error), alpha=0)
    plt.legend(frameon=True, framealpha=0.9, fontsize=10)
    plt.axis('square')
    plt.show()

# Llamar a la función y mostrar el área y el error
mc_pi_aprox(50000)
