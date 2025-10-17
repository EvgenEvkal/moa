#Begin39 Вершинин ИСП 111
A = float(input("Введите A: "))
B = float(input("Введите B: "))
C = float(input("Введите C: "))
if a != 0:
    D = B ** 2 - 4 * A * C
    if D > 0:
        x1 = (-b - D ** 0,5) / (2  * a)
        x2 = (-b + D ** 0,5) / (2 * a)
    print("x1 =" , x1)
    print("x2 =" , x2)
    elif D == 0:
        x1 = (-b - D ** 0,5) / (2 * a)
        print("x1 =" , x1)
    else:
        print("Корней нету!")
else:
    print("Коэффициент А не должен быть равен 0!")