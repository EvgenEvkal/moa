#Boolean23 Вершинин ИСП111
A = int(input())
A1 = A // 1000
A2 = (A // 100) % 10
A3 = (A % 100) // 10
A4 = A % 10
print(A1 == A4 and A2 == A3)