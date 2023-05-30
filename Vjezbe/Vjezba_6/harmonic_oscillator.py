import numpy as np
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self, m, k, x0, v0, dt, t):
        self.m = m
        self.k = k
        self.w = np.sqrt(k/m)
        self.x0 = x0
        self.v0 = v0
        self.dt = dt
        self.t = t
        self.t_niz = np.arange(0, self.t, self.dt)
        self.x = [self.x0]
        self.v = [self.v0]
        self.a = [- (self.k / self.m) * self.x0]
        self.analiticko_x = self.x0 * np.cos(self.w * self.t_niz) + (self.v0 / self.w) * np.sin(self.w * self.t_niz)
        self.analiticko_v = -self.x0 * self.w * np.sin(self.w * self.t_niz) + self.v0 * np.cos(self.w * self.t_niz)
        self.analiticko_a = -self.x0 * self.w**2 * np.cos(self.w * self.t_niz) - self.v0 * self.w * np.sin(self.w * self.t_niz)
        self.move()

    def move(self):
        for i in range(1, len(self.t_niz)):
            self.a.append(- (self.k / self.m) * self.x[i-1])
            self.v.append(self.v[i-1] + self.a[i] * self.dt)
            self.x.append(self.x[i-1] + self.v[i] * self.dt)
    
    def plot_trajectory(self):
        plt.title('Harmonijski oscilator')  

        plt.subplot(1, 3, 1)
        plt.scatter(self.t_niz, self.x, label="Numeričko rješenje", s=3.5, c="k")
        plt.plot(self.t_niz, self.analiticko_x, label="Analitičko rješenje", c="y")
        plt.title("x-t graf")
        plt.xlabel("t [s]")
        plt.ylabel("x [m]")

        plt.subplot(1, 3, 2)
        plt.scatter(self.t_niz, self.v, label="Numeričko rješenje", s=3.5, c="k")
        plt.plot(self.t_niz, self.analiticko_v, label="Analitičko rješenje", c="y")
        plt.title("v-t graf")
        plt.xlabel("t [s]")
        plt.ylabel("v [m/s]")
        
        plt.subplot(1, 3, 3)
        plt.scatter(self.t_niz, self.a, label="Numeričko rješenje", s=3.5, c="k")
        plt.plot(self.t_niz, self.analiticko_a, label="Analitičko rješenje", c="y")
        plt.title("a-t graf")
        plt.xlabel("t [s]")
        plt.ylabel("a [m/s^2]")
        
        plt.tight_layout()
        plt.show()
        
#imam trenutno problema sa racunanjem perioda titranja. vratit cu se tome kad izvrsim sve obaveze u sklopu ovog predmeta. vec sam cijeli dan izgubio na jednu vjezbu.