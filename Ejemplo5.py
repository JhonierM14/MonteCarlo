import numpy as np

np.random.seed(2023)  # Semilla para replicar la aleatoriedad

# retorna la estimacion del numero de soluciones y la posicion de las tuplas
def soluciones(x, y, E, N):
    soluciones = 0
    lista_index = []

    # el punto evaluado en un index i es el mismo en ambas funciones
    for i in range(N):
        if(abs(x[i]) < E and abs(y[i]) < E):
            soluciones +=1
            lista_index.append(i)

    return soluciones, lista_index

def simulacionfun(E, N):
    var = 0
    # se crean puntos aleatorios uniformes
    x = np.random.uniform(-2, 2, N)
    y = np.random.uniform(-2, 2, N)

    # se crean funciones con los valores
    f1 = np.sin(x) + np.cos(x)
    f2 = x**2 - y

    # se estima la cantidad de soluciones
    estimacion, puntosSolucion = soluciones(f1, f2, E, N)

    # se buscan las tuplas solucion
    tuplasSolucion= []

    for i in puntosSolucion: 
        tuplasSolucion.append((x[i], y[i]))
        var = 1
    if var != 0:    
        print(f"se estiman: {estimacion} soluciones\n"
          f"tuplas solucion encontradas: {tuplasSolucion}\n")

# Para visualizar como varia la precision de la estimacion
def analizarPrecision():
    numSimulaciones = 1000
    i = 0
    E = 0.0001; N = 1000
    while(i < numSimulaciones):
        simulacionfun(E, N)
        N += 10000
        print(N)
        i += 1

analizarPrecision()
