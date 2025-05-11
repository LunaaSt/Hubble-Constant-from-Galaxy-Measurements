import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import sys

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


c = 299729  # km/s

#Less galaxies
galaxias = pd.DataFrame([
    {"nombre": "ANTENNAE", "z": 0.00547,  "d": 27.900, "m": 10.91 , "B-V": 0},
    {"nombre": "CENTAURUS A", "z": 0.001826, "d": 4.900, "m": 6.84, "B-V": 1.34},
    {"nombre": "IC 2738", "z": 0.05360,  "d": 213.000, "m": 15.30 , "B-V":0},
    {"nombre": "LGS 3", "z": 0.000955,  "d": 1.198,  "m": 14.30, "B-V": 1.88},
    {"nombre": "M31", "z": -0.001000,  "d": 778.000,  "m": 3.40, "B-V": 0.96},
    {"nombre": "M32", "z": -0.000664,  "d": 763.000,  "m": 8.10, "B-V": 0.93},
    {"nombre": "M33", "z": -0.000598,  "d": 835.000,  "m": 5.70, "B-V": 0.57},
    {"nombre": "M49", "z": 0.003393,  "d": 17.700, "m": 8.40, "B-V": 4.81},
    {"nombre": "M58", "z": 0.005047,  "d": 19.100,  "m": 9.66, "B-V": 0.82},
    {"nombre": "M60", "z": 0.003690,  "d": 16.800, "m": 8.80, "B-V": 1.50},
    {"nombre": "M61", "z": 0.005240,  "d": 16.100, "m": 9.65, "B-V": 0.53},
    {"nombre": "M66", "z": 0.002349,  "d": 11.000, "m": 8.90, "B-V": 0.75},
    {"nombre": "M74", "z": 0.002188,  "d": 9.200,  "m": 9.40, "B-V": 0.55},
    {"nombre": "M77", "z": 0.003810,  "d": 14.400,  "m": 8.90, "B-V": 0.71},
    {"nombre": "M84", "z": 0.003369,  "d": 18.400,  "m": 9.10, "B-V": 2.99},
    {"nombre": "M87", "z": 0.004233,  "d": 18.400,  "m": 8.60, "B-V": 0.99},
    {"nombre": "M88", "z": 0.007602,  "d": 14.410,  "m": 9.60, "B-V": 4.73},
    {"nombre": "M94", "z": 0.000960,  "d": 4.910,  "m": 8.20, "B-V": 0.79},
    {"nombre": "M95", "z": 0.002595,  "d": 10.000,  "m": 9.70, "B-V": 0.83},
    {"nombre": "M96", "z": 0.003012,  "d": 9.600, "m": 9.30, "B-V": 0.91},
    {"nombre": "M99", "z": 0.008036,  "d": 15.400, "m": 9.90, "B-V": 0.54},
    {"nombre": "M100", "z": 0.005250,  "d": 16.860, "m": 9.40, "B-V": 0.65},
    {"nombre": "M104", "z": 0.003642,   "d": 8.980, "m": 8.00, "B-V": 0.98},
    {"nombre": "M105", "z": 0.002922,   "d": 9.800, "m": 9.30, "B-V": 1.26},
    {"nombre": "M106", "z": 0.001541,   "d": 7.000, "m": 8.40, "B-V": 0.70},
    {"nombre": "M108", "z": 0.002328,   "d": 14.100, "m": 10.00, "B-V": 0.70},
    {"nombre": "M110", "z": -0.000820,   "d": 824.000, "m": 8.10, "B-V": 0.82},
    {"nombre": "NGC 300", "z": 0.000487,  "d": 1.980, "m": 8.13, "B-V": 0.56},
    {"nombre": "NGC 891", "z": 0.001761,   "d": 9.120, "m": 10.10, "B-V": 0.71},
    {"nombre": "NGC 1260", "z": 0.018400,  "d": 77.000, "m": 13.53, "B-V": 0.67},
    {"nombre": "NGC 1270", "z": 0.016690,  "d": 53.700, "m": 13.32, "B-V": 1.08},
    {"nombre": "NGC 1271", "z": 0.012850,  "d": 53.700, "m": 13.66, "B-V": 0.84},
    {"nombre": "NGC 1275", "z": 0.017560,  "d": 68.900, "m": 12.48, "B-V": 0.62},
    {"nombre": "NGC 1316", "z": 0.005911,  "d": 16.900, "m": 8.53, "B-V": 0.62},
    {"nombre": "NGC 1512", "z": 0.002782,  "d": 14.300,"m": 10.32, "B-V": 0.76},
    {"nombre": "NGC 1672", "z": 0.004464,  "d": 14.500, "m": 9.68, "B-V": 0.85},
    {"nombre": "NGC 1705", "z": 0.002112,  "d": 6.000, "m": 12.39, "B-V": 0.43},
    {"nombre": "NGC 3079", "z": 0.003766,  "d": 22.600, "m": 10.86, "B-V": 0.68},
    {"nombre": "NGC 3115", "z": 0.002222,  "d": 13.300, "m": 9.90, "B-V": 1.10},
    {"nombre": "NGC 3226", "z": 0.004230,  "d": 23.400, "m": 13.33, "B-V": 0.99},
    {"nombre": "NGC 3227", "z": 0.003650,  "d": 23.700, "m": 11.79, "B-V": 0.82},
    {"nombre": "NGC 3310", "z": 0.003366,  "d": 22.900, "m": 12.15, "B-V": 0.30},
    {"nombre": "NGC 3370", "z": 0.004276,  "d": 31.200, "m": 12.40, "B-V": 0.00},
    {"nombre": "NGC 3808", "z": 0.023603,  "d": 116.000, "m": 14.10, "B-V": 14.10},
    {"nombre": "NGC 4005", "z": 0.014890,  "d": 81.200, "m": 13.44, "B-V": 0.66},
    {"nombre": "NGC 4556", "z": 0.025221,  "d": 114.000, "m": 14.40, "B-V": 0.00},
    {"nombre": "NGC 4860", "z": 0.026470,  "d": 67.600,  "m": 13.24, "B-V": 1.46},
    {"nombre": "NGC 4881", "z": 0.022526,  "d": 127.000,  "m": 13.56, "B-V": 1.14},
    {"nombre": "NGC 5643", "z": 0.003990,  "d": 16.900,   "m": 13.60, "B-V": -2.57},
    {"nombre": "NGC 6907", "z": 0.010649,  "d": 45.000,  "m": 11.30, "B-V": 0.61},
])
def v_rel(z): return c * z


#Hubble's Law
galaxias["v"] = v_rel(galaxias["z"])
galaxias["H"] = galaxias["v"] / galaxias["d"]

#obtainig M for each galaxy from M = m - 5log(d) + 5

print("MAGNITUDES ABSOLUTAS")
galaxias["M"] = galaxias["m"] - 5 *np.log10(galaxias["d"] * pow(10,6)) + 5
for index, g in galaxias.iterrows():
    print(f"{g['nombre']}: M = {g['M']:.2f}")
#If we'd like to know the maximum value of M and the name of that galaxy, we use the following
max_M = galaxias.iloc[galaxias["M"].idxmax()]
print(f"\nLa galaxia con mayor magnitud absoluta es:  {max_M['nombre']} con M = {max_M['M']:.2f}")

#Same thing but this time with the luminosity and the maximum
print("LUMINOSIDAD DE LAS GALAXIAS")
M_0 = -20.9
L_via_lactea = 2e28  #W
galaxias["L"] = 10**((galaxias["M"] - M_0) / -2.5)

for index, g in galaxias.iterrows():
    print(f"{g['nombre']}: L / L_Vía_Láctea = {g['L']:.2f}")

max_luminosidad = galaxias.iloc[galaxias["L"].idxmax()]
print(f"\nLa galaxia con mayor luminosidad es {max_luminosidad['nombre']} con L = {max_luminosidad['L']:.2f}", "L via lactea ")
#Now we want to know the minimum of B-V intead of idmax use idmin
azul = galaxias.iloc[galaxias["B-V"].idxmin()]
print(f"\nLa galaxia más azul es {azul['nombre']} con B-V = {azul['B-V']:.2f}")

print("La lonfitud de onda con z mayor")
lambda_emitida = 6562.8  #Å

g_max = galaxias.iloc[galaxias["z"].idxmax()]
lambda_obs = lambda_emitida * (1 + g_max["z"])

print(f"{g_max['nombre']}: z = {g_max['z']:.5f}, λ_obs(Hα) = {lambda_obs:.2f} Å")

#build the latex table form this
latex_table = """\\begin{table}[h!]
\\centering
\\begin{tabular}{||c|c|c|c|c|c|c||}
\\hline
Nombre & $z$ & $d$ [Mpc] & $V_c$ [km/s] & $H_0$ [Km/s/Mpc] & $(B-V)$ & M & $L/L_{VL}$ [W] \\\\
\\hline"""

for index, galaxia in galaxias.iterrows():
    latex_table += f"\n{galaxia['nombre']} & {galaxia['z']} & {galaxia['d']} & {galaxia['v']} & {galaxia['H']} & {galaxia['B-V']} & {galaxia['M']} & {galaxia['L']} \\\\ \\hline"

latex_table += """
\\hline
\\end{tabular}
\\end{table}
"""
print(latex_table)






