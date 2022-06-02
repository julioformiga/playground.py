def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num - 1)


def baskara(a, b, c):
    delta = (b**2) - (4*a*c)
    if delta < 0:
        print("Delta negativo")
    else:
        x1 = (-b + (delta**0.5))/(2*a)
        x2 = (-b - (delta**0.5))/(2*a)
        print(x1, x2)


def main():
    num = int(input("Digite um número: "))
    print(fatorial(num))


if __name__ == "__main__":
    main()
