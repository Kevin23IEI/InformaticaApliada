import numpy as np
import matplotlib.pyplot as plt
# Generamos una muestra aleatoria de una distribución uniforme
uniforme = np.random.uniform(low=0, high=1, size=1000)
# Generamos una muestra aleatoria de una distribución normal
normal = np.random.normal(loc=0, scale=1, size=1000)
# Generamos una muestra aleatoria de una distribución de Poisson
poisson = np.random.poisson(lam=5, size=1000)
# Generamos una muestra aleatoria de una distribución binomial
binomial = np.random.binomial(n=10, p=0.5, size=1000)
# Graficamos las distribuciones
fig, axs = plt.subplots(2, 2, figsize=(10,10))
axs[0, 0].hist(uniforme, bins=20)
axs[0, 0].set_title('Distribución uniforme')
axs[0, 1].hist(normal, bins=20)
axs[0, 1].set_title('Distribución normal')
axs[1, 0].hist(poisson, bins=20)
axs[1, 0].set_title('Distribución de Poisson')
axs[1, 1].hist(binomial, bins=20)
axs[1, 1].set_title('Distribución binomial')
plt.show()