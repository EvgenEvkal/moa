#Begin37 Вершинин ИСП 111
V1 = float(input())
V2 = float(input())
S = float(input())
T = float(input())
if V1 >= 0 and V2 >= 0 and S >= 0 and T >= 0:
    S -= V1 * T + V2 * T
    print(abs(S))
else:
    print("Один из аргументов отрицательный!")