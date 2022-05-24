n = int(input("Informe um número\n"))
while(n >= 0):
    res = 1
    while(n > 0):
        res = res * n
        n = n - 1
    print(res)
    n = int(input("Informe um número\n"))
