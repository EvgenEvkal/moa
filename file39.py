#Begin39 Вершинин ИСП 111
A = float(input("Введите A: "))
B = float(input("Введите B: "))
C = float(input("Введите C: "))
if A != 0:
    D = B ** 2 - 4 * A * C
    if D > 0:
        x1 = (-B - D ** 0.5) / (2  * A)
        x2 = (-B + D ** 0.5) / (2 * A)
        print("x1 =" , x1)
        print("x2 =" , x2)
    elif D == 0:
        x1 = -B / (2 * A)
        print("x1 =" , x1)
    else:
        print("Корней нету!")
else:
    print("Коэффициент A не должен быть равен 0!")