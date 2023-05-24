def jednadzba_pravca(x1, y1, x2, y2):

    k = (y2 - y1) / (x2 - x1)

    l = y1 - k * x1

    print("Jednadžba pravca: y = {}x + {}". format(k, l))

x1 = float(input("Unesite x koordinatu 1. točke: "))
y1 = float(input("Unesite y koordinatu 1. točke: "))

x2 = float(input("Unesite x koordinatu 2. točke: "))
y2 = float(input("Unesite y koordinatu 2. točke: "))

jednadzba_pravca(x1, y1, x2, y2)