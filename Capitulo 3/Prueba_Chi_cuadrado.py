import numpy as np
from scipy.stats import chi2_contingency
# Creamos una tabla de contingencia con datos aleatorios
tabla = np.array([[10, 20, 30],
                   [20, 30, 10], 
                   [30, 10, 20]])
#fo es un elemento dentro de la formula 


# Realizamos la prueba de chi-cuadrado para determinar si hay una relación significativa
# entre las filas y las columnas de la tabla
chi2, pvalue, dof, expected = chi2_contingency(tabla)
# Imprimimos los resultados
print("Estadístico chi-cuadrado:", chi2)
print("Valor p:", pvalue)