import numpy as np
import matplotlib.pyplot as plt
import math

class Particle:
    def __init__(self, v0, alfa, x0, y0):
        self.v0 = v0
        self.alfa = alfa
        self.x0 = x0
        self.y0 = y0
        self.vx = v0 * math.cos(alfa * math.pi / 180)
        self.vy = v0 * math.sin(alfa * math.pi / 180)
        self.x = x0
        self.y = y0
        
    def reset(self):
        self.vx = self.v0 * math.cos(self.alfa * math.pi / 180)
        self.vy = self.v0 * math.sin(self.alfa * math.pi / 180)
        self.x = self.x0
        self.y = self.y0
        
    def __move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt - 0.5 * 9.81 * dt**2
        self.vy += -9.81 * dt
        
    def range(self, dt):
        while self.y >= 0:
            self.__move(dt)
            
        domet = self.x - self.x0
        self.reset()
        return domet
    
    def plot_trajectory(self, dt):
        x_os = []
        y_os = []
        
        while self.y >= 0:
            x_os.append(self.x)
            y_os.append(self.y)
            self.__move(dt)
            
        plt.plot(x_os, y_os)
        plt.xlabel("x os [m]")
        plt.ylabel("y os [m]")
        plt.title("Putanja čestice")
        plt.show()