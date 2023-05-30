import numpy as np
import statistics as stat

#1. Calcular la media, mediana y desviación estándar de un conjunto de datos:
#datos = np.array([5, 7, 8, 9, 10, 11, 12, 14, 15, 16])


# Creamos una lista de datos
datos = np.array([5, 7, 8, 9, 10, 11, 12, 14, 15, 16])
# Calculamos la media
media = np.mean(datos)
# Calculamos la mediana
mediana = np.median(datos)
# Calculamos la moda
# moda = np.mode(datos)
#moda = stat.mode(datos)
# Calculamos la desviación estándar
desv_estandar = np.std(datos)
# Calculamos la varianza
#varianza = np.var(datos)
# Imprimimos los resultados
print("\n---Ejercicio 1---")
print("Media:", media)
print("Mediana:", mediana)
#print("Moda:", moda)
print("Desviación estándar:", desv_estandar)
#print("Varianza:", varianza)


#2. Calcular el coeficiente de variación de un conjunto de datos:
#datos = np.array([5, 7, 8, 9, 10, 11, 12, 14, 15, 16])

# Creamos una lista de datos
datos2 = np.array([5, 7, 8, 9, 10, 11, 12, 14, 15, 16,17,18,19,20])
# Calculamos la media
media2 = np.mean(datos)
# Calculamos la desviación estándar
desv_estandar2 = np.std(datos)
#Calculamos el coeficiente de variación
CV=(desv_estandar2/media2)*100
# Imprimimos los resultados
print("\n--Ejercicio 2---")
print("Coeficiente de variación:", CV)
print("\n")
