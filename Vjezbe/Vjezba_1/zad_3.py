def unos():
    while True:
        a = input("Unesite x koordinatu točke: ")
        b = input("Unesite y koordinatu točke: ")

        if a.isdigit() and b.isdigit():
            x = float(a)
            y = float(b)
            return x, y
        else:
            print("Ponovite unos.")

print("Unesite koordinate 1. točke: ")
x1, y1 = unos()

print("Unesite koordinate 2. točke: ")
x2, y2 = unos()

k = (y2 - y1) / (x2 - x1)
l = y1 - k * x1

print("Jednadžba pravca: y = {}x + {}".format(k, l))