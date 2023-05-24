import numpy as np
import matplotlib.pyplot as plt

def funkcija(x1, y1, x2, y2, graf=False, ime_datoteke=""):

    k = (y2 - y1) / (x2 - x1)

    l = - k * x1 + y1

    print("Jednadžba pravca: y = {}x + {} ". format(k, l))

    min_x = min(x1, x2)
    max_x = max(x1, x2)

    min_y = k * min_x + l
    max_y = k * max_x + l

    plt.plot(x1, y1, marker="o", label="Točka 1")
    plt.plot(x2, y2, marker="o", label="Točka 2")

    plt.plot([min_x, max_x], [min_y, max_y], label="Pravac")

    plt.xlabel("x os")
    plt.ylabel("y os")
    plt.legend()

    if graf:
        plt.show()
    elif ime_datoteke:
        plt.savefig("{}.pdf".format(ime_datoteke))

x1 = float(input("Unesite x koordinatu 1. točke: "))
y1 = float(input("Unesite y koordinatu 1. točke: "))

x2 = float(input("Unesite x koordinatu 2. točke: "))
y2 = float(input("Unesite y koordinatu 2. točke: "))

odabir = input("Želite li prikazati graf (P) ili ga spremiti kao PDF (S)? ")

if odabir == 'P':
    funkcija(x1, y1, x2, y2, graf=True)
elif odabir == 'S':
    ime_datoteke = input("Unesite ime datoteke: ")
    funkcija(x1, y1, x2, y2, graf=False, ime_datoteke=ime_datoteke)
