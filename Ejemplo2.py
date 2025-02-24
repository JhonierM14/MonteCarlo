import numpy as np
import matplotlib.pyplot as plt

# Parámetro distribución exponencial (tasa de atención)
lambda_val = 2  # caso base: 2 clientes por minuto

# Generar muestras de la distribución exponencial
N = 50000  # Número de muestras
samples = np.random.exponential(1/lambda_val, size=N)

# Calcular el valor esperado E[T]
valor_esperado = np.mean(samples)
print(f'Valor esperado E[T] estimado: {valor_esperado:.4f} minutos')

# Graficar la distribución teórica y las muestras generadas
x = np.linspace(0, np.max(samples), 100)
pdf = lambda_val * np.exp(-lambda_val * x)

plt.figure(figsize=(8, 8))
plt.plot(x, pdf, 'r-', lw=3, label='Distribución Exponencial')
plt.hist(samples, bins=30, density=True, alpha=0.6, color='b', label='Muestras generadas')
plt.xlabel('$T$', fontsize=12)
plt.ylabel('$pdf(T)$', fontsize=12)
plt.legend(fontsize=12)
plt.show()
