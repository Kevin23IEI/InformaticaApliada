#Tarea de codigo comentado acerca de señales analógicas y digitales
#Informatica Aplicada

# filtro Digital pasa bajos Butterworth 
"""El filtro Butterworth es un tipo de filtro de procesamiento de señal diseñado para
     tener una respuesta de frecuencia lo más plana posible en la banda de paso. """""
"""""
Las especificaciones son las siguientes: 

Tasa de muestreo de 40 kHz
Frecuencia de borde de banda de paso de 4 kHz
Frecuencia de borde de banda de parada de 8kHz
Ondulación de banda de paso de 0,5 dB
Atenuación mínima de la banda de parada de 40 dB

Graficar la respuesta en frecuencia, fase e impulso del filtro.
"""
#Importacion de bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import math


#DEfinimos las especificaciones del filtro 
# definimos la frecuencia de muestreo
f_sample = 40000 

# Definimos la frecuencia de banda de paso 
f_pass = 4000  
  
# DEfinimos la frecuencia de corte
f_stop = 8000  
  
# frecuencia de rizado de la banda de paso
fs = 0.5
  
# frecuencia de banda de paso en radianes
wp = f_pass/(f_sample/2)  
  
# frecuencia de corte de la banda en radianes
ws = f_stop/(f_sample/2) 
  
# tiempo de muestreo
Td = 1  
  
 #rizado de la banda de paso
g_pass = 0.5 
  
# atenuecion de corte de la banda 
g_stop = 40  
  
#Construcción del filtro usando la función signal.buttord 
# Conversión a frecuencia analógica 
omega_p = (2/Td)*np.tan(wp/2)
omega_s = (2/Td)*np.tan(ws/2)
  
  
# Diseño de filtro usando la función Signal.Buttord
N, Wn = signal.buttord(omega_p, omega_s, g_pass, g_stop, analog=True)
  
  
#Imprimimos los valores de orden y frecuencia de corte
print("Orden del Filtro=", N)  # N es el orden
#Wn es la frecuencia de corte del filtro
print("Frecuencia de corte= {:.3f} rad/s ".format(Wn))
  
  
# Conversión en dominio Z
#Diseñamos el filtros Butterworth. 
#  b es el numerador del filtro y a es el denominador
b, a = signal.butter(N, Wn, 'low', True)
#Con .bilinear Devolvemos un filtro IIR (Respuestas al impulso infinito) digital a partir de uno analógico
# utilizando una transformada bilineal.
z, p = signal.bilinear(b, a, fs)
#Calculamos la respuesta en frecuencia de un filtro digital.
# w es la frecuencia en el dominio z y h es la magnitud en el dominio z
w, h = signal.freqz(z, p, 512)
  
# Trazado de la Respuesta de Magnitud. 
# Respuesta de magnitud
#Graficamos los datos obtenidos y le asignamos nombres a los ejes
#así como la configuración grafica de los ejes
plt.semilogx(w, 20*np.log10(abs(h)))
plt.xscale('log')
plt.title('Respuesta en frecuencia del filtro Butterworth')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(100, color='green')
plt.show()
  
#Representación gráfica de la respuesta al impulso  
# Respuesta impulsiva
#Graficamos los datos obtenidos y le asignamos nombres a los ejes
#así como la configuración grafica de los ejes
imp = signal.unit_impulse(40)
c, d = signal.butter(N, 0.5)
response = signal.lfilter(c, d, imp)
plt.stem(np.arange(0, 40), imp, use_line_collection=True)
plt.stem(np.arange(0, 40), response, use_line_collection=True)
plt.margins(0, 0.1)
plt.title('Respuesta al impulso')
plt.xlabel('Tiempo [muestras]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()
  
#Trazado de la respuesta de fase  
# Respuesta de fase
#Graficamos los datos obtenidos y le asignamos nombres a los ejes
#así como la configuración grafica de los ejes
fig, ax1 = plt.subplots()
ax1.set_title('Respuesta en frecuencia del filtro digital')
ax1.set_ylabel('Angulo(radianes)', color='g')
ax1.set_xlabel('Frequencia [Hz]')
angles = np.unwrap(np.angle(h))
ax1.plot(w/2*np.pi, angles, 'g')
ax1.grid()
ax1.axis('tight')
plt.show()