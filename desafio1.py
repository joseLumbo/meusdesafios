def escada_1(n):
    for k in range(1, n + 1):
        for i in range(n, k, -1):
            print("", end = " ")
        for z in range(0, k):
            print("*", end = '')
        print()

escada_1(10)