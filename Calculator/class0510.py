import math

acc = 0.0
while 1:
    n = input(f"[ acc == {acc} ] [ введите число или действие: ]\n")

    if n == "exit":
        break
    elif n == "=":
        print(f"{acc}")
    elif n == "C":
        acc = 0.0
        print("[ сброшено ]")

    elif n in ("+", "-", "*", "/", "**"):
        m = float(input(f"[ введите число: ]\n"))
        if n == "+":
                acc = acc + m
        elif n == "-":
                acc = acc - m
        elif n == "*":
                acc = acc * m
        elif n == "**":
                acc = acc ** m
        elif n == "/":
            if m == 0:
                print("[ на ноль делить нельзя ]")
                break
            else:
                acc = acc / m

    elif n in ("sin()", "sin"):
        acc = math.sin(acc)
    elif n in ("cos()", "cos"):
        acc = math.cos(acc)

    else:
        try:
            acc = float(n)
        except:
            print("[ ошибка ]")


