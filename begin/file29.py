#BEGIN29 | Туйчиева, Вершинин ИСП 111
a = float(input("Введите a: "))
if a > 0 and a < 360:
    radian = (a * 3.14)/180
    print(a , "градусов в радианах =" , radian)
else:
    print("Ваше значение превышает лимит!")