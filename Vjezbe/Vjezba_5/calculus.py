import numpy as np

def derivacija(f, x, epsilon=0.01, metoda=3):
    if metoda == 2:
        return (f(x + epsilon) - f(x)) / epsilon
    elif metoda == 3:
        return (f(x + epsilon) - f(x - epsilon)) / (2 * epsilon)

def derivacija_raspon(f, donja, gornja, epsilon=0.01, metoda=3):
    dx = []
    x = []
    
    for i_x in np.arange(donja, gornja, epsilon):
        x.append(i_x)
        dx.append(derivacija(f, i_x, epsilon, metoda))
    return x, dx



def pravokutna_aproksimacija(f, donja, gornja, n):
    donja_suma = 0
    gornja_suma = 0
    dx = abs((gornja - donja) / n)

    for i in range(1, n):
        donja_suma += f(donja + i * dx) * dx

    for i in range(1, n+1):
        gornja_suma += f(donja + i * dx) * dx

    return donja_suma, gornja_suma

def trapezna_formula(f, donja, gornja, n):
    suma = 0.5*(f(donja) + f(gornja))
    dx = abs((gornja - donja) / n)
    
    for i in range(1, n):
        suma += f(donja + i*dx)
        
    return suma * dx