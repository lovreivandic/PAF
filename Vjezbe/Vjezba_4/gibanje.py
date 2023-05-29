from particle import Particle
import math

v0 = 12
alfa = 66
x0 = 0
y0 = 0

cestica = Particle(v0, alfa, x0, y0)

domet = cestica.range(0.01)
analiticki_domet = (v0 ** 2 * math.sin(2 * alfa * math.pi / 180)) / 9.81
rel_gre = ((domet - analiticki_domet) / domet) * 100

print("Domet je {} m.".format(domet))
print("Analitički domet je {} m.".format(analiticki_domet))
print("Relativna pogreška iznosi {}%.".format(rel_gre))

cestica.plot_trajectory(0.01)