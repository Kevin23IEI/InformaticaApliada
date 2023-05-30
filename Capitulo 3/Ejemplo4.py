import numpy as np
from scipy.stats import norm
from statsmodels.base.model import GenericLikelihoodModel
# Definimos la función de verosimilitud para la distribución normal
class NormalLikelihood(GenericLikelihoodModel):
    def loglike(self, params):
        mu = params[0]
        sigma = params[1]
        return norm.logpdf(self.endog, mu, sigma).sum()
# Generamos una muestra aleatoria de una distribución normal
datos = norm.rvs(loc=0, scale=1, size=1000)
# Estimamos los parámetros de la distribución normal utilizando el método de máxima verosimilitud
modelo = NormalLikelihood(datos)
resultado = modelo.fit(start_params=[0, 1])
mu_estimado, sigma_estimado = resultado.params
# Imprimimos los parámetros estimados
print('Parámetros estimados:')
print(f'mu = {mu_estimado}')
print(f'sigma = {sigma_estimado}')