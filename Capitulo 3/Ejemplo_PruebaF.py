import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Definir los grados de libertad para la distribución F
dfn = 3
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Definir los grados de libertad para la distribución F
dfn = 3  # grados de libertad del numerador
dfd = 10  # grados de libertad del denominador

# Generar una distribución F
x = np.linspace(0, 5, 1000)
y = stats.f.pdf(x, dfn, dfd)


# Graficar la distribución F
plt.plot(x, y)
plt.fill_between(x, 0, y, where=(x >= stats.f.ppf(0.05, dfn, dfd)), color='red', alpha=0.5)
plt.fill_between(x, 0, y, where=(x >= stats.f.ppf(0.01, dfn, dfd)), color='blue', alpha=0.5)
plt.title('Distribución F con {} y {} grados de libertad'.format(dfn, dfd))
plt.xlabel('Valor F')
plt.ylabel('Densidad')
plt.show()