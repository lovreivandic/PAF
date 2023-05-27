import math
import numpy as np
import matplotlib.pyplot as plt

v0 = float(input("Unesi početnu brzinu v0 u [m/s]: "))
theta = float(input("Unesi kut otklona Θ u [°]: "))
g = -9.81

t = [0]
x = [0]
y = [0]
v_x = [v0 * math.cos(math.radians(theta))]
v_y = [v0 * math.sin(math.radians(theta))]
a_x = [0]
a_y = [g]

for i in range(10):
    a_x.append(0)
    a_y.append(g)
    t.append((i + 1))
    v_x.append(v_x[i] + a_x[i])
    v_y.append(v_y[i] + a_y[i])
    x.append(x[i] + v_x[i])
    y.append(y[i] + v_y[i])

plt.subplot(1, 3, 1)
plt.plot(x, y)
plt.title("x-y graf")
plt.xlabel("x [m]")
plt.ylabel("y [m]")

plt.subplot(1, 3, 2)
plt.plot(t, x)
plt.title("x-t graf")
plt.xlabel("t [s]")
plt.ylabel("x [m]")

plt.subplot(1, 3, 3)
plt.plot(t, y)
plt.title("y-t graf")
plt.xlabel("t [s]")
plt.ylabel("y [m]")

plt.tight_layout()
plt.show()