import numpy as np
import matplotlib.pyplot as plt

# Define the carrier signal
fc = 10
t = np.linspace(0, 1, 1000)
carrier = np.cos(2 * np.pi * fc * t)

# Define the message signal
fm = 2
message = np.cos(2 * np.pi * fm * t)

# Modulate the message onto the carrier signal
modulated = carrier * (1 + 0.5 * message)

# Plot the signals
plt.plot(t, carrier, label='Carrier')
plt.plot(t, message, label='Message')
plt.plot(t, modulated, label='Modulated')
plt.legend()
plt.show()