import math
import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(F, m):
 
    t = [0]
    x = [0]
    v = [0]
    a = [F / m]

    for i in range(10):
        t.append((i + 1))
        a.append(F / m)
        v.append(v[i] + a[i])
        x.append(x[i] + v[i])

    plt.subplot(1, 3, 1)
    plt.plot(t, x)
    plt.title("x-t graf")
    plt.xlabel("t [s]")
    plt.ylabel("x [m]")

    plt.subplot(1, 3, 2)
    plt.plot(t, v)
    plt.title("v-t graf")
    plt.xlabel("t [s]")
    plt.ylabel("v [m/s]")

    plt.subplot(1, 3, 3)
    plt.plot(t, a)
    plt.title("a-t graf")
    plt.xlabel("t [s]")
    plt.ylabel("a [m/s^2]")

    plt.tight_layout()
    plt.show()
    

def kosi_hitac(v0, theta):

    g = -9.81
    
    t = [0]
    x = [0]
    y = [0]
    v_x = [v0 * math.cos(math.radians(theta))]
    v_y = [v0 * math.sin(math.radians(theta))]
    a_x = [0]
    a_y = [g]
    
    for i in range(10):
        a_x.append(0)
        a_y.append(g)
        t.append((i + 1))
        v_x.append(v_x[i] + a_x[i])
        v_y.append(v_y[i] + a_y[i])
        x.append(x[i] + v_x[i])
        y.append(y[i] + v_y[i])
    
    plt.subplot(1, 3, 1)
    plt.plot(x, y)
    plt.title("x-y graf")
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")

    plt.subplot(1, 3, 2)
    plt.plot(t, x)
    plt.title("x-t graf")
    plt.xlabel("t [s]")
    plt.ylabel("x [m]")

    plt.subplot(1, 3, 3)
    plt.plot(t, y)
    plt.title("y-t graf")
    plt.xlabel("t [s]")
    plt.ylabel("y [m]")

    plt.tight_layout()
    plt.show()