#Begin33 Вершинин ИСП 111
X = float(input("Введите кол-во конфет(кг): "))
A = float(input("Введите общую стоимость: "))
Y = float(input("Введите кол-во конфет(кг): "))
one_kg = A/X
Y_kg = Y * one_kg
print("Цена за 1 кг:" , one_kg)
print("Стоимость" , Y , "кг конфет:" , Y_kg)