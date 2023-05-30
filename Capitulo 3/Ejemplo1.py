import numpy as np
import statistics as stat

# Creamos una lista de datos
datos = np.array([10, 12, 15, 18, 20, 22, 24, 28, 30, 30])
# Calculamos la media
media = np.mean(datos)
# Calculamos la mediana
mediana = np.median(datos)
# Calculamos la moda
# moda = np.mode(datos)
moda = stat.mode(datos)
# Calculamos la desviación estándar
desv_estandar = np.std(datos)
# Calculamos la varianza
varianza = np.var(datos)
# Imprimimos los resultados
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print("Desviación estándar:", desv_estandar)
print("Varianza:", varianza)