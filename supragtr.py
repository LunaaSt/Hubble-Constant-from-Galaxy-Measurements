import numpy as np
import matplotlib.pyplot as plt
""""
# Crear una matriz diagonal de ejemplo
matrix_size = 200
diagonal_values = np.random.rand(matrix_size) * 100  # Genera valores aleatorios para la diagonal
diagonal_matrix = np.diag(diagonal_values)

# Crear una figura y ejes
fig, ax = plt.subplots()

# Mostrar la matriz diagonal con un mapa de colores
cax = ax.matshow(diagonal_matrix, cmap='gray')

# Añadir barra de color para indicar la escala
fig.colorbar(cax)

# Mostrar la imagen
plt.show()

m_n = 939.5636

factor = 931.494 #para que este en unidades MeV/c^2

m_H = 1.008  * factor

m_Li_7 = 7.01600 * factor
m_Li_6 = 6.015122 * factor

m_zr_90 = 89.90470 * factor
m_zr_91 = 90.90564 * factor

m_u_236 = 236.0455 * factor
m_u_235 = 235.0439 * factor

S_zr = (m_zr_90 - m_zr_91 + m_n)
S_Li = (m_Li_6 - m_Li_7 + m_n)
S_u = (m_u_235 - m_u_236 + m_n)

print(S_Li, "MeV - Litio"
      ,"\n",
      S_zr, "MeV - Circonio"
      ,"\n",
      S_u , "MeV - Uranio")

m_Ne_z = 18.9984 * factor
m_ne = 19.99244 * factor

m_mn = 54.9380 * factor
m_mn_z = 53.938 * factor


S_Ne = (m_Ne_z - m_ne + m_H)
S_mn = (m_mn_z - m_mn + m_H)

print(S_Ne, "MeV - Neon"
      ,"\n",
      S_mn, "MeV - Magnesio")


#helio Z = 2 A = 3
m_he = 3.016029 * factor
b = 1/3 * (2*m_H + m_n - m_he )
print(b, "Mev/nucleon - Energia de enlace del Helio-3")


print(3 * m_n,"Mev del neutron" , "\n", m_H, "Mev del hidrogeno")
"""


