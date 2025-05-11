
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import sys

c = 299729  # speed of light [km/s]

# Galaxy data from Stellarium
galaxias = pd.DataFrame([
    {"nombre": "ANTENNAE", "z": 0.00547, "d": 27.900, "m": 10.91, "B-V": 0},
    {"nombre": "CENTAURUS A", "z": 0.001826, "d": 4.900, "m": 6.84, "B-V": 1.34},
    {"nombre": "IC 2738", "z": 0.05360, "d": 213.000, "m": 15.30, "B-V": 0},
    {"nombre": "LGS 3", "z": 0.000955, "d": 1.198, "m": 14.30, "B-V": 1.88},
   #{"nombre": "M31", "z": -0.001000, "d": 778.000, "m": 3.40, "B-V": 0.96}, We dont take into account these galaxies due to z<0 to obtain H
    #{"nombre": "M32", "z": -0.000664, "d": 763.000, "m": 8.10, "B-V": 0.93},
    #{"nombre": "M33", "z": -0.000598, "d": 835.000, "m": 5.70, "B-V": 0.57},
    {"nombre": "M49", "z": 0.003393, "d": 17.700, "m": 8.40, "B-V": 4.81},
    {"nombre": "M58", "z": 0.005047, "d": 19.100, "m": 9.66, "B-V": 0.82},
    {"nombre": "M60", "z": 0.003690, "d": 16.800, "m": 8.80, "B-V": 1.50},
    {"nombre": "M61", "z": 0.005240, "d": 16.100, "m": 9.65, "B-V": 0.53},
    {"nombre": "M66", "z": 0.002349, "d": 11.000, "m": 8.90, "B-V": 0.75},
    {"nombre": "M74", "z": 0.002188, "d": 9.200, "m": 9.40, "B-V": 0.55},
    {"nombre": "M77", "z": 0.003810, "d": 14.400, "m": 8.90, "B-V": 0.71},
    {"nombre": "M84", "z": 0.003369, "d": 18.400, "m": 9.10, "B-V": 2.99},
    {"nombre": "M87", "z": 0.004233, "d": 18.400, "m": 8.60, "B-V": 0.99},
    {"nombre": "M88", "z": 0.007602, "d": 14.410, "m": 9.60, "B-V": 4.73},
    {"nombre": "M94", "z": 0.000960, "d": 4.910, "m": 8.20, "B-V": 0.79},
    {"nombre": "M95", "z": 0.002595, "d": 10.000, "m": 9.70, "B-V": 0.83},
    {"nombre": "M96", "z": 0.003012, "d": 9.600, "m": 9.30, "B-V": 0.91},
    {"nombre": "M99", "z": 0.008036, "d": 15.400, "m": 9.90, "B-V": 0.54},
    {"nombre": "M100", "z": 0.005250, "d": 16.860, "m": 9.40, "B-V": 0.65},
    {"nombre": "M104", "z": 0.003642, "d": 8.980, "m": 8.00, "B-V": 0.98},
    {"nombre": "M105", "z": 0.002922, "d": 9.800, "m": 9.30, "B-V": 1.26},
    {"nombre": "M106", "z": 0.001541, "d": 7.000, "m": 8.40, "B-V": 0.70},
    {"nombre": "M108", "z": 0.002328, "d": 14.100, "m": 10.00, "B-V": 0.70},
    #{"nombre": "M110", "z": -0.000820, "d": 824.000, "m": 8.10, "B-V": 0.82},
    {"nombre": "NGC 300", "z": 0.000487, "d": 1.980, "m": 8.13, "B-V": 0.56},
    {"nombre": "NGC 891", "z": 0.001761, "d": 9.120, "m": 10.10, "B-V": 0.71},
    {"nombre": "NGC 1260", "z": 0.018400, "d": 77.000, "m": 13.53, "B-V": 0.67},
    {"nombre": "NGC 1270", "z": 0.016690, "d": 53.700, "m": 13.32, "B-V": 1.08},
    {"nombre": "NGC 1271", "z": 0.012850, "d": 53.700, "m": 13.66, "B-V": 0.84},
    {"nombre": "NGC 1275", "z": 0.017560, "d": 68.900, "m": 12.48, "B-V": 0.62},
    {"nombre": "NGC 1316", "z": 0.005911, "d": 16.900, "m": 8.53, "B-V": 0.62},
    {"nombre": "NGC 1512", "z": 0.002782, "d": 14.300, "m": 10.32, "B-V": 0.76},
    {"nombre": "NGC 1672", "z": 0.004464, "d": 14.500, "m": 9.68, "B-V": 0.85},
    {"nombre": "NGC 1705", "z": 0.002112, "d": 6.000, "m": 12.39, "B-V": 0.43},
    {"nombre": "NGC 3079", "z": 0.003766, "d": 22.600, "m": 10.86, "B-V": 0.68},
    {"nombre": "NGC 3115", "z": 0.002222, "d": 13.300, "m": 9.90, "B-V": 1.10},
    {"nombre": "NGC 3226", "z": 0.004230, "d": 23.400, "m": 13.33, "B-V": 0.99},
    {"nombre": "NGC 3227", "z": 0.003650, "d": 23.700, "m": 11.79, "B-V": 0.82},
    {"nombre": "NGC 3310", "z": 0.003366, "d": 22.900, "m": 12.15, "B-V": 0.30},
    {"nombre": "NGC 3370", "z": 0.004276, "d": 31.200, "m": 12.40, "B-V": 0.00},
    {"nombre": "NGC 3808", "z": 0.023603, "d": 116.000, "m": 14.10, "B-V": 14.10},
    {"nombre": "NGC 4005", "z": 0.014890, "d": 81.200, "m": 13.44, "B-V": 0.66},
    {"nombre": "NGC 4556", "z": 0.025221, "d": 114.000, "m": 14.40, "B-V": 0.00},
    {"nombre": "NGC 4860", "z": 0.026470, "d": 67.600, "m": 13.24, "B-V": 1.46},
    {"nombre": "NGC 4881", "z": 0.022526, "d": 127.000, "m": 13.56, "B-V": 1.14},
    {"nombre": "NGC 5643", "z": 0.003990, "d": 16.900, "m": 13.60, "B-V": -2.57},
    {"nombre": "NGC 6907", "z": 0.010649, "d": 45.000, "m": 11.30, "B-V": 0.61},
    {"nombre": "3C 273", "z":   0.158340,  "d": 657.800},
    {"nombre": "ESO 254-3", "z":0.052690,  "d": 231.140},
    {"nombre": "ESO 291-6", "z": 0.08651, "d": 354.000},
    {"nombre": "ESO 410-6", "z": 0.10934,  "d": 440.550},
    {"nombre": "LEDA 1964358", "z": 0.22983, "z_err": 0.000001, "d": 1060.750},
    {"nombre": "LEDA 1163616", "z": 0.11264,  "d": 481.640},
    {"nombre": "LEDA 2816758", "z": 0.1778,  "d": 736.600},
    {"nombre": "MGC-02-02-026", "z": 0.05400,  "d": 193.410},
    {"nombre": "MGC-03-03-004", "z": 0.05518, "d": 197.485},
    {"nombre": "Mrk 540", "z": 0.07114,  "d": 304.79}
])

# Recessional velocity of the galaxy
def v_rel(z): return c * z


# Hubble's Law
galaxias["v"] = v_rel(galaxias["z"])
galaxias["H"] = galaxias["v"] / galaxias["d"]

#Average of H from all galaxies
H0_prom  =np.sum(galaxias["H"]) / len(galaxias)
print("el promedio de todas las galaxias es:", H0_prom , "Km/s/Mpc")


numerador = np.sum(galaxias["d"] * galaxias["v"])
denominador = np.sum(galaxias["d"]**2)
H0 = numerador / denominador  #slope
invert_H0 = denominador/numerador #Age of the universe without unit conversion
Edad = (invert_H0 * 3.086 * pow(10,19)) / (3.154 * pow(10,7))

print("La pendiente de Hublle es:", H0, "Km/s/Mpc \n",
      "La edad del universo: ", Edad , "años")

#Linear regression
x_fit = np.linspace(0, galaxias["d"].max(), 100)
y_fit = H0 * x_fit

x = np.linspace(0, galaxias["d"].max(), 100)
y = np.linspace(0, galaxias["v"].max(), 100)

H0 = np.sum(galaxias["d"] * galaxias["v"]) / np.sum(galaxias["d"]**2)
v_fit = H0 * x

H0_inv = np.sum(galaxias["v"] * galaxias["d"]) / np.sum(galaxias["v"]**2)
d_fit = H0_inv * y

# Subplots [0] is v-d and [1] the inverse d-v then we obtain two plots in 1row 2 cols format
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].scatter(galaxias["d"], galaxias["v"], color='blue', label="Datos")
axs[0].plot(x, v_fit, color='red', label=f"v = {H0:.1f} d")
axs[0].set_title("Constante de Hubble")
axs[0].set_xlabel("Distancia [Mpc]")
axs[0].set_ylabel("Velocidad [km/s]")
axs[0].legend()
axs[0].grid(True)

axs[1].scatter(galaxias["v"], galaxias["d"], color='black', label="Datos")
axs[1].plot(y, d_fit, color='purple', label=f"d = {H0_inv:.4f} v")
axs[1].set_title("Edad del universo")
axs[1].set_xlabel("Velocidad [km/s]")
axs[1].set_ylabel("Distancia [Mpc]")
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()

#make a latex table includig the galaxies with negative z
latex_table = """\\begin{table}[h!]
\\centering
\\begin{tabular}{||c|c|c||}
\\hline
Nombre & $z$ & $d$ [Mpc] \\\\
\\hline"""

for index, galaxia in galaxias.iterrows():
    latex_table += f"\n{galaxia['nombre']} & {galaxia['z']} & {galaxia['d']} \\\\ \\hline"

latex_table += """
\\end{tabular}
\\end{table}
"""
print(latex_table)

#Save all the prints in a txt file from os
output_path = os.path.join(os.getcwd(), "output.txt")

print(f"Archivo de salida: {output_path}")

class Tee:
    def __init__(self, name):
        self.file = open(name, "w")
        self.stdout = sys.stdout
        sys.stdout = self

    def write(self, data):
        self.stdout.write(data)
        self.file.write(data)

    def flush(self):
        self.stdout.flush()
        self.file.flush()

    def close(self):
        sys.stdout = self.stdout
        self.file.close()

tee = Tee(output_path)
#On macOS, to open the file, open Finder and press Cmd + Shift + G, then paste the path you obtained from the code
#only the file will save this part from below intead the code of the latex table, you will get galaxy: z , d ...

for _, g in galaxias.iterrows():
    print(f"{g['nombre']}: z = {g['z']:.5f}, d = {g['d']:.2f} Mpc, v = {g['v']:.0f} km/s, m = {g['m']:.2f}, H = {g['H']:.2f}, B-V = {g['B-V']:.2f}")



