#Begin35 Вершинин ИСП 111
V = float(input())
U = float(input())
T1 = float(input())
T2 = float(input())
if U < V and U > 0 and V > 0 and T1 > 0 and T2 > 0:
    S = T1 * V + T2 * (V - U)
    print(S)
else:
    print("Какой-то аргумент меньше 0 или равен 0 или скорость реки больше скорости лодки!")