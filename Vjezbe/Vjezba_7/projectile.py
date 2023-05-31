import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    g = -9.81
    rho_zrak = 1.225

    def __init__(self, v, alfa, m, otpor, A, dt):
        self.m = m
        self.otpor = otpor
        self.A = A
        self.dt = dt
        self.v_x = [v * np.cos(np.radians(alfa))]
        self.v_y = [v * np.sin(np.radians(alfa))]
        self.a_x = [0]
        self.a_y = [self.g]
        self.x = [0]
        self.y = [0]

    def move(self):
        while self.y[-1] >= 0:
            self.x.append(self.x[-1] + self.v_x[-1] * self.dt)
            self.y.append(self.y[-1] + self.v_y[-1] * self.dt)
            self.v_x.append(self.v_x[-1] + self.a_x[-1] * self.dt)
            self.v_y.append(self.v_y[-1] + self.a_y[-1] * self.dt)
            self.a_x.append(-1 * np.sign(self.v_x[-1]) * ((self.rho_zrak * self.otpor * self.A) / (2 * self.m)) * self.v_x[-1]**2)
            self.a_y.append(self.g - 1 * np.sign(self.v_y[-1]) * ((self.rho_zrak * self.otpor * self.A) / (2 * self.m)) * self.v_y[-1]**2)

    def f_x(self, v_x):
        return -1 * np.sign(v_x) * ((self.rho_zrak * self.otpor * self.A) / (2 * self.m)) * v_x**2

    def f_y(self, v_y):
        return self.g - 1 * np.sign(v_y) * ((self.rho_zrak * self.otpor * self.A) / (2 * self.m)) * v_y**2

    def move_RK4(self):
        while self.y[-1] >= 0:
            k1vx = self.f_x(self.v_x[-1]) * self.dt
            k1x = self.v_x[-1] * self.dt
            k2vx = self.f_x(self.v_x[-1] + 0.5 * k1vx) * self.dt
            k2x = (self.v_x[-1] + 0.5 * k1vx) * self.dt  
            k3vx = self.f_x(self.v_x[-1] + 0.5 * k2vx) * self.dt
            k3x = (self.v_x[-1] + 0.5 * k2vx) * self.dt
            k4vx = self.f_x(self.v_x[-1] + k3vx) * self.dt
            k4x = (self.v_x[-1] + k3vx) * self.dt

            k1vy = self.f_y(self.v_y[-1]) * self.dt
            k1y = self.v_y[-1] * self.dt
            k2vy = self.f_y(self.v_y[-1] + 0.5 * k1vy) * self.dt
            k2y = (self.v_y[-1] + 0.5 * k1vy) * self.dt  
            k3vy = self.f_y(self.v_y[-1] + 0.5 * k2vy) * self.dt
            k3y = (self.v_y[-1] + 0.5 * k2vy) * self.dt
            k4vy = self.f_y(self.v_y[-1] + k3vy) * self.dt
            k4y = (self.v_y[-1] + k3vy) * self.dt
            
            self.x.append(self.x[-1] + (k1x + 2*k2x + 2*k3x + k4x)/6)
            self.v_x.append(self.v_x[-1] + (k1vx + 2*k2vx + 2*k3vx + k4vx)/6)
            
            self.y.append(self.y[-1] + (k1y + 2*k2y + 2*k3y + k4y)/6)
            self.v_y.append(self.v_y[-1] + (k1vy + 2*k2vy + 2*k3vy + k4vy)/6)

    def plot_trajectory(self):
        plt.title("Kosi hitac s otporom zraka dt={:.2f}".format(self.dt))  
        plt.plot(self.x, self.y, label = "Euler")
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.show()
        
    def plot_trajectory_RK4(self):
        plt.title("Kosi hitac s otporom zraka")  
        plt.plot(self.x, self.y, label = "Runge-Kutta 4. reda")
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.show()