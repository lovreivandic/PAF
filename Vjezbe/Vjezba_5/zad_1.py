import calculus
import numpy as np
import matplotlib.pyplot as plt

donja = float(input("Unesite donju granicu derivacije: "))
gornja = float(input("Unesite gornju granicu derivacije: "))
epsilon = 0.01

def kub(x):
    return x**3 - 2 * x**2 + x + 4

def trig(x):
    return np.sin(x)

def d_a_kub(x):
    return 3 * x**2 - 4 * x + 1

def d_a_trig(x):
    return np.cos(x)

x = np.arange(donja, gornja, epsilon)

x_kub, d_kub = calculus.derivacija_raspon(kub, donja, gornja, epsilon)
x_trig, d_trig = calculus.derivacija_raspon(trig, donja, gornja, epsilon)

plt.subplot(1, 2, 1)
plt.plot(x, d_a_kub(x), label="Analitička derivacija")
plt.plot(x_kub, d_kub, label="Numerička derivacija")
plt.title("Kubna funkcija")
plt.xlabel("x os")
plt.ylabel("y os")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x, d_a_trig(x), label="Analitička derivacija")
plt.plot(x_trig, d_trig, label="Numerička derivacija")
plt.title("Trigonometrijska funkcija")
plt.xlabel("x os")
plt.ylabel("y os")
plt.legend()

plt.tight_layout()
plt.show()