import numpy as np
import matplotlib.pyplot as plt

m1 = 5.9742e24
m2 = 1.989e30

class SolarniSistem:
    def __init__(self, m1, m2, godina=365.242*24*3600, dt=3600):
        self.G = 6.67408e-11
        self.m1 = m1
        self.m2 = m2
        self.godina = godina
        self.dt = dt
        self.t = 0
        
        self.r1 = np.array([1.486e11, 0.0])
        self.r2 = np.array([0.0, 0.0])
        self.v1 = np.array([0.0, 29783.0])
        
        dx = self.r1[0] - self.r2[0]
        dy = self.r1[1] - self.r2[1]
        r = np.sqrt(dx**2 + dy**2)
        
        self.a1 = -self.G * self.m2 * (self.r1-self.r2) / r**3

        self.x1 = [self.r1[0]]
        self.y1 = [self.r1[1]]

    def move(self):
        while self.t <= self.godina:
            self.v1 += self.a1 * self.dt
            self.r1 += self.v1 * self.dt
            
            dx = self.r1[0] - self.r2[0]
            dy = self.r1[1] - self.r2[1]
            r = np.sqrt(dx**2 + dy**2)
            
            self.a1 = -self.G * self.m2 * (self.r1-self.r2) / r**3
            
            self.x1.append(self.r1[0])
            self.y1.append(self.r1[1])
            
            self.t += self.dt

    def plot_trajectory(self):
        plt.plot(self.x1, self.y1, color="b", label="Zemlja")
        plt.scatter(0, 0, color="r", label="Sunce")
        plt.legend()
        plt.show()

sim = SolarniSistem(m1, m2)
sim.move()
sim.plot_trajectory()
