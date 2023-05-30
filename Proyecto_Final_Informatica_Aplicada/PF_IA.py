
"""
Mayo 2023
INFORMÁTICA APLICADA
PROYECTO FINAL:
    "Análisis estadístico de datos de la flor Iris"
KEA
"""

import pandas as pd
import numpy as np
import statistics as stat
import matplotlib.pyplot as plt

datos=pd.read_csv("C:/Users/pc/Desktop/Informatica Aplicada/InformaticaApliada/Proyecto_Final_Informatica_Aplicada/dataset/iris.csv", 
                  header=0 )#index_col=())
print(datos)

LS=(datos['sepal.length'])
print("\nLargo del Sépalo\n",LS)

AS=(datos['sepal.width'])
print("\nAncho del Sépalo\n",AS)

LP=(datos['petal.length'])
print("\nLargo del Pétalo\n",LP)

AP=(datos['petal.width'])
print("\nAncho del Sépalo\n",AP)

Especie=(datos['variety'])
print("\nVaiedades\n",Especie)
#print(type(Especie[149]))
#print(AP[145])#para accedder a un valor específico

#############Estadística descriptiva
#Promedio

media=np.zeros(shape=4) #creamos un vector de ceros para guardar las medias

for i in range (0,4,1):
    media[i]=np.mean(datos[datos.columns[i]])
print("Promedios:",
      "\nLargo Sépalo:",media[0],
      "\nAncho Sépalo:",media[1], 
      "\nLargo Pétalo:",media[2],
      "\nAncho Pétalo:",media[3])
#print(media[:])


####desviación estándar

desv_estandar=np.zeros(shape=4) #creamos un vector de ceros para guardar las medias

for j in range (0,4,1):
    desv_estandar[j]=np.std(datos[datos.columns[j]])
#print(desv_estandar[:])
print("\nDesviaciones Estándar:",
      "\nLargo Sépalo:",desv_estandar[0],
      "\nAncho Sépalo:",desv_estandar[1], 
      "\nLargo Pétalo:",desv_estandar[2],
      "\nAncho Pétalo:",desv_estandar[3])

##maximos
maximo=np.zeros(shape=4)
for m in range (0,4,1):
    maximo[m]=max(datos[datos.columns[m]])
#print(maximo[:])
print("\nMáximos:",
      "\nLargo Sépalo:",maximo[0],
      "\nAncho Sépalo:",maximo[1], 
      "\nLargo Pétalo:",maximo[2],
      "\nAncho Pétalo:",maximo[3])


###minimos 

minimo=np.zeros(shape=4)
for s in range (0,4,1):
    minimo[s]=min(datos[datos.columns[s]])
#print(minimo[:])
print("\nMínimos:",
      "\nLargo Sépalo:",minimo[0],
      "\nAncho Sépalo:",minimo[1], 
      "\nLargo Pétalo:",minimo[2],
      "\nAncho Pétalo:",minimo[3])


#Visualización de datos

#Histogramas
#longitud=len(LP)
#print(longitud)
"""
plt.hist(Especie, bins=10, color="red")
plt.title('Distribución de especies')
plt.xlabel('Especies')
plt.ylabel('Frecuencia')
plt.show()
"""

plt.hist(LP[0:50], bins=10,  color="green")
plt.title('Distribución de longitudes de los pétalos de la especie Setosa')
plt.xlabel('Longitud')
plt.ylabel('Frecuencia')
plt.show()

plt.hist(LP[51:100], bins=10,  color="purple")
plt.title('Distribución de longitudes de los pétalos de la especie Versicolor')
plt.xlabel('Longitud')
plt.ylabel('Frecuencia')
plt.show()

plt.hist(LP[101:150], bins=10, color="blue")
plt.title('Distribución de longitudes de los pétalos de la especie Virginica')
plt.xlabel('Longitud')
plt.ylabel('Frecuencia')
plt.show()

#Finalmente graficamos todas las longitudes en un solo gráfico
plt.hist(LP[0:50], label='Setosa',color="green")
plt.hist(LP[51:100], label='Versicolor', color="purple")
plt.hist(LP[101:150], label='Virginica', color="blue")
plt.title('Distribución de longitudes de los pétalos')
plt.xlabel('Longitud')
plt.ylabel('Frecuencia')
plt.legend(loc='upper right')
plt.show()

####2. Diagrama de dispersión de longitud del sépalo vs. ancho del sépalo
plt.scatter(LS, AS)
plt.title('Longitud del Sépalo vs. Ancho del Sépalo')
plt.xlabel('Longitud ')
plt.ylabel('Ancho ')
plt.show()

plt.scatter(LP, AP)
plt.title('Longitud del Pétalo vs. Ancho del Pétalo')
plt.xlabel('Longitud ')
plt.ylabel('Ancho ')
plt.show()

#3. Correlación entre las variables

# Calcular el coeficiente de correlación Sépalo Longitud y anchura
corr_coef = np.corrcoef(LS,AS)[0, 1]
# Graficar los datos
plt.scatter(LS,AS)
plt.title(f'Coeficiente de correlación (Sépalo): {corr_coef:.2f}')
plt.xlabel('Longitud de Sépalo')
plt.ylabel('Ancho de Sépalo')
plt.show()

# Calcular el coeficiente de correlación Pétalo Longitud y anchura
corr_coef2 = np.corrcoef(LP,AP)[0, 1]
# Graficar los datos
plt.scatter(LP,AP)
plt.title(f'Coeficiente de correlación (Pétalo): {corr_coef2:.2f}')
plt.xlabel('Longitud de Pétalo')
plt.ylabel('Ancho de Pétalo')
plt.show()


"""
import csv
f=open("C:/Users/pc/Desktop/Informatica Aplicada/InformaticaApliada/Proyecto_Final_Informatica_Aplicada/dataset/iris.csv")
reader=csv.reader(f)
for row in reader:
    print(row)


"""
