import math

def aritmetička_sredina(točke):
    arit = sum(točke) / len(točke)
    return arit
    

def standardna_devijacija(točke):
    arit = aritmetička_sredina(točke)
    dev = math.sqrt((sum((x - arit) ** 2 for x in točke)) / (len(točke)*(len(točke)-1)))
    return dev

točke = []
for i in range(10):
    unos = float(input("Unesite brojeve: "))
    točke.append(unos)

print("Aritmetička sredina: {}".format(aritmetička_sredina(točke)))

print("Standardna devijacija: {}".format(standardna_devijacija(točke)))