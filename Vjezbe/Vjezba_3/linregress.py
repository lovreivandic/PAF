import numpy as np
import matplotlib.pyplot as plt
import statistics as st
import math

M = np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336])
φ = np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472])

xy = []
x2 = []
y2 = []

for i in range(len(M)):
    xy.append(φ[i] * M[i])
    x2.append(φ[i] ** 2)
    y2.append(M[i] ** 2)

a = st.mean(xy) / st.mean(x2)
σa = math.sqrt((1 / len(M)) * (st.mean(y2) / st.mean(x2) - a ** 2))

print("Modul torzije Dt iznosi: {} ± {}". format(a, σa))

plt.scatter(φ, M, label="Modul torzije")
plt.plot(φ, a * φ, label="Regresijska linija")
plt.xlabel("φ [rad]")
plt.ylabel("M [Nm]")
plt.show()