import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

"""
x = np.linspace(-5, 5, 1000)
t = np.linspace(-5, 5, 1000)

q_c = -1 #cerrado eliptica
q_a1 = 1 #abierto plana
q_a2 = 1/2 #abierto hiperbólico

t_c = 1 / ( np.sqrt(q_c/x**2 - q_c +1))
t_a1 = 1 / ( np.sqrt(q_a1/x**2 - q_a1 +1))
t_a2 = 1 / ( np.sqrt(q_a2/x**2 - q_a2 +1))

plt.plot(x,t_c , c="red", label="$q_0=-1$")
plt.plot(x,t_a1 , c="blue", label="$q_0=1$")
plt.plot(x,t_a2 , c="green", label="$q_0=1/2$")
plt.grid()
plt.legend(loc = "upper right")
plt.title("Tiempo cosmológico: $t = \\frac{1}{H_0} \int _0^{R/R_0} (\\frac{q_0}{x^2}-q_0+1 )dx$")
plt.ylabel("Tiempo")
plt.xlabel("$x= \\frac{R}{R_0}$")
#plt.show()
"""
print("Gracias Ropas por fundar TrigoDulce")

#values
c = 3 * pow(10,8)
e = 1.6 * pow(10,-19)
epsilon = 8.85 * pow(10,-12)
R = 41 #radius
#v =  float(input("Inserte el valor de v: ")) * c
v_frac = float(input("Inserte el valor de v : "))  # e.g. 0.01 o 0.9999
v = v_frac * c

#Equations
gamma = 1 / np.sqrt(1 - (v**2/c**2)) #Gamma Factor
a = pow(v,2) / R
P = (e**2 * a**2 * pow(gamma,6) ) / (6 * np.pi * epsilon * pow(c,3)) #Larmor Power
T = (2* np.pi * R) / v #time to complete the cyle
E = P * T #Emitted energy per cyle
print("The Larmor Power:", P, "W",
      "\n Time to complete the cyle: " , T, "s",
      "\n The energy emitted per cyle: ", E,"J", "in eV" , E/e, "eV")
print("the velocity: " , v, "m/s")

#integral solving
me = 9.1 * pow(10,-31) #electron mass
v_0 = 0.01 * c #initial velocity
t = lambda v : -(6 * np.pi * epsilon * pow(c,3) * pow(R,2))/(pow(e,2) * pow(v,4) * pow(gamma,6)) * (v*me*c**2)/(pow(c,2) * pow(1-v**2/c**2,3/2))
result, error = quad(t, v_0, 0.99*v_0)
print("Resultado de la integral:", result)
