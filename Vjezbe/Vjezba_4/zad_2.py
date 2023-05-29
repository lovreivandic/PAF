from particle import Particle
import matplotlib.pyplot as plt
import math

cestica = Particle(10, 60, 0, 0)

analiticki_domet = (10 ** 2 * math.sin(2 * 60 * math.pi / 180)) / 9.81

dt_vrijednosti = []
rel_pogreska = []
dt = 0.01

while dt <= 1:
    domet = cestica.range(dt)

    rel_gre = abs((domet - analiticki_domet) / domet) * 100
    rel_pogreska.append(rel_gre)
    dt_vrijednosti.append(dt)
    
    dt += 0.01
    cestica.reset()

plt.plot(dt_vrijednosti, rel_pogreska)
plt.xlabel("∆t [s]")
plt.ylabel("Relativna pogreška [%]")
plt.title("Ovisnost relativne pogreške o vrijednosti vremenskog koraka")
plt.show()