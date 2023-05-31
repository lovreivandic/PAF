from projectile import Projectile
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(16, 9))

dt_ovi = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09]

for dt in dt_ovi:
    proj = Projectile(v=100, alfa=45, m=1, otpor=0.47, A=1, dt=dt)
    proj.move()
    
    ax = fig.add_subplot(3, 3, int(dt * 100))
    ax.plot(proj.x, proj.y, label = "Euler")
    ax.set_title("Kosi hitac s otporom zraka dt={:.2f}".format(proj.dt))
    ax.set_xlabel("x [m]")
    ax.set_ylabel("y [m]")
    
plt.tight_layout()
plt.show()

# vidimo da pri dt=0.05 graf pocinje izgledati cudno i ne izgleda kao fizikalno gibanje na koje smo navikli. zapravo izgleda kao da se hitac odbio od zid
# delta t postaje privisok u ovom slucaju i zbog same visoke brzine pa razlika izmedu polozaja dvaju uzastopnih tocaka je velika i dobivamo cudno gibanje
# to se najbolje vidi ako koristimo ax.scatter umjesto ax.plot