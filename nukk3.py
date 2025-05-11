import math
import numpy as np
from matplotlib import pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

# Constantes
G = 6.67430e-11     # Constante gravitacional (m^3 kg^-1 s^-2)
c = 3.0e8           # Velocidad de la luz (m/s)
M = 1.989e30        # Masa (por ejemplo, del Sol)
rs = 2 * G * M / c**2  # Radio de Schwarzschild

# Rango de radios
r = np.linspace(1.1 * rs, 20 * rs, 1000)

# Diferentes valores de L_z (momento angular)
L_values = [1e10, 2e10, 3e10, 4e10]

# Plot
plt.figure(figsize=(10, 6))

for L in L_values:
    Veff = - (rs * c**2) / (2 * r) + (L**2 / (2 * c**2 * r**2)) * (1 - rs / r)
    plt.plot(r / rs, Veff / c**2, label=f'L = {L:.1e}')

plt.axhline(0, color='gray', linestyle='--')
plt.xlabel(r'$r / r_s$')
plt.ylabel(r'$V_{\mathrm{ef}}(r) / c^2$')
plt.title('Potencial efectivo en Schwarzschild para distintos $L_z$')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
