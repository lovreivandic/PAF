from projectile import Projectile
import matplotlib.pyplot as plt

proj_euler = Projectile(v=100, alfa=45, m=1, otpor=0.47, A=1, dt=0.01)
proj_RK4 = Projectile(v=100, alfa=45, m=1, otpor=0.47, A=1, dt=0.01)

proj_euler.move()
proj_RK4.move_RK4()

plt.title("Usporedba metoda Euler i Runge-Kutta")
plt.plot(proj_euler.x, proj_euler.y, label="Euler")
plt.plot(proj_RK4.x, proj_RK4.y, label="Runge-Kutta")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.legend()
plt.show()