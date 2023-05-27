import statistics

točke = []
for i in range(10):
    unos = float(input("Unesite brojeve: "))
    točke.append(unos)

arit = statistics.mean(točke)
dev = statistics.stdev(točke)

print("Aritmetička sredina: {}".format(arit))

print("Standardna devijacija: {}".format(dev))