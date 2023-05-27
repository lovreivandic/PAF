import numpy as np
import matplotlib.pyplot as plt

F = float(input("Unesi silu F u [N]: "))
m = float(input("Unesi masu čestice m u [kg]: "))

t = [0]
x = [0]
v = [0]
a = [F / m]

for i in range(10):
    t.append((i + 1))
    a.append(F / m)
    v.append(v[i] + a[i])
    x.append(x[i] + v[i])

plt.subplot(1, 3, 1)
plt.plot(t, x)
plt.title("x-t graf")
plt.xlabel("t [s]")
plt.ylabel("x [m]")

plt.subplot(1, 3, 2)
plt.plot(t, v)
plt.title("v-t graf")
plt.xlabel("t [s]")
plt.ylabel("v [m/s]")

plt.subplot(1, 3, 3)
plt.plot(t, a)
plt.title("a-t graf")
plt.xlabel("t [s]")
plt.ylabel("a [m/s^2]")

plt.tight_layout()
plt.show()