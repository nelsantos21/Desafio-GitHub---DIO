import math

def delta(a,b,c):
    return b**2 - 4 * a * c

def imprime_raizes(a,b,c):
    d = delta(a,b,c)
    if d == 0:
        raiz = (-b + math.sqrt(delta))/(2*a)
        print("A única raiz é: ",raiz)
    else:
        if d < 0:
            print("Esta equação não possui raizes reais, pois o delta é menor que zero")
        else:    
            raiz1 = (-b + math.sqrt(d))/(2*a)
            raiz2 = (-b - math.sqrt(d))/(2*a)
            print("A primeira raiz é:", raiz1)
            print("A segunda raiz é:", raiz2)

def main():
    a = float(input("Digite o valor de a:\n"))
    b = float(input("Digite o valor de b:\n"))
    c = float(input("Digite o valor de c:\n"))
    imprime_raizes(a,b,c)

main()


