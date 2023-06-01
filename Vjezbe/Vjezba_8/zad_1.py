import numpy as np
import matplotlib.pyplot as plt

class particle:
    def __init__(self, q, m, v, E, B, dt=0.01):
        self.E = E
        self.B = B
        self.q = q
        self.m = m
        self.v = np.array(v)
        self.x = [0.0]
        self.y = [0.0]
        self.z = [0.0]
        self.t = [0.0]
        self.dt = dt

    def __move(self):
        self.a = (self.q/self.m) * (self.E + np.cross(self.v, self.B))
        self.v += self.a * self.dt
        self.x.append(self.x[-1] + self.v[0] * self.dt)
        self.y.append(self.y[-1] + self.v[1] * self.dt)
        self.z.append(self.z[-1] + self.v[2] * self.dt)
        self.t.append(self.t[-1] + self.dt)

    def calculate_trajectory(self, t):
        t0 = 0
        while t0 < t:
            self.__move()
            self.x.append(self.x[-1] + self.v[0] * self.dt)
            self.y.append(self.y[-1] + self.v[1] * self.dt)
            self.z.append(self.z[-1] + self.v[2] * self.dt)
            t0 += self.dt
        return self.x, self.y, self.z

q = 1
m = 1
v = [10.0, 6.0, 3.0]
E = [0, 0, 0]
B = [0, 0, 1]
dt = 0.01
t = 20

elektron = particle(-q, m, v, E, B, dt)
elektron.calculate_trajectory(t)

pozitron = particle(q, m, v, E, B, dt)
pozitron.calculate_trajectory(t)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection="3d")

ax.plot(elektron.x, elektron.y, elektron.z, label="Elektron")
ax.plot(pozitron.x, pozitron.y, pozitron.z, label="Pozitron")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.legend()
plt.show()