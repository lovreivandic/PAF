import calculus
import numpy as np
import matplotlib.pyplot as plt

donja = float(input("Unesite donju granicu integracije: "))
gornja = float(input("Unesite gornju granicu integracije: "))
n = 100

dolje = []
gore = []
trapez = []

def kvad(x):
    return x**2 + 2 * x + 4 

def int_kvad(x):
    return (1/3) * x**3 + x**2 + 4 * x

x = np.arange(1, n+1, 1)

for i in x:
    donja_suma, gornja_suma = calculus.pravokutna_aproksimacija(kvad, donja, gornja, i)
    dolje.append(donja_suma)
    gore.append(gornja_suma)
    trapez.append(calculus.trapezna_formula(kvad, donja, gornja, i))
    
analiticki_integral = int_kvad(gornja) - int_kvad(donja)

y = kvad(x)
plt.title("Integrali")
plt.xlabel("N")
plt.ylabel("Vrijednost integrala")
plt.plot([donja, gornja], [analiticki_integral, analiticki_integral], label="Analitički integral")
plt.plot(x, dolje, label = "Donja integralna suma")
plt.plot(x, gore, label = "Gornja integralna suma")
plt.plot(x, trapez, label = "Metoda trapeza")
plt.legend()
plt.show()