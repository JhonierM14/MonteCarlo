import matplotlib.pyplot as plt
import numpy as np

np.random.seed(2023)  # Semilla para replicar la aleatoriedad

n = int(input("Ingrese la cantidad de puntos aleatorios a generar: "))

## definir una ecuacion por intervalos para una figura irregular

def mc_Af_aprox(N):
    plt.figure(figsize=(8, 8))
    x = np.random.uniform(-np.pi, np.pi, N)
    y = np.random.uniform(-np.pi, 1, N)

    interior_izquierdo = (y <= np.abs(np.sin(x))) & (y >= np.abs(x) - np.pi) & (x <= 0)
    interior_derecho = (y <= np.sin(x)) & (y >= (np.abs(x) - np.pi)) & (x >= 0)

    exterior = y <= 1
    area_rectangulo = (2*np.pi)*(np.pi+1)
    
    # Aproximación del área de la figura irregular
    Area_irregular = ( ( interior_izquierdo.sum() + interior_derecho.sum() ) * area_rectangulo / (N) ) 
    error = abs((Area_irregular - (pow(np.pi, 2) + 4)) / (pow(np.pi, 2) + 4)) * 100


    plt.plot(x[exterior], y[exterior], 'y.')
    plt.plot(x[interior_izquierdo], y[interior_izquierdo], 'k.')
    plt.plot(x[interior_derecho], y[interior_derecho], 'k.')
    plt.title(f'Aproximación Monte Carlo del área de la figura con {N} puntos')
    plt.plot(0, 0, label='$\hat Af$ = {:4.4f}\nerror = {:4.4f}%'
            .format(Area_irregular, error), alpha=0)
    plt.legend(frameon=True, framealpha=0.9, fontsize=10)
    plt.axis('square')
    plt.show()
        
# Llamar a la función y mostrar el área y el error
mc_Af_aprox(n)
