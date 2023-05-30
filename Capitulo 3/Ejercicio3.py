import numpy as np
from scipy.stats import gamma
# Generamos una muestra aleatoria de una distribución gamma
datos = gamma.rvs(a=2, loc=0, scale=1, size=1000)
# Estimamos los parámetros de la distribución gamma utilizando el método de los momentos
media = np.mean(datos)
varianza = np.var(datos)
alfa = media**2 / varianza
beta = media / varianza
# Imprimimos los parámetros estimados
print('Parámetros estimados:')
print(f'alfa = {alfa}')
print(f'beta = {beta}')