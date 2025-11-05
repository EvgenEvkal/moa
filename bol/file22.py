#Boolean22 Вершинин ИСП111
A = int(input())
A1 = A // 100
A2 = (A % 100) // 10
A3 = A % 10
print(A1 < A2 and A2 > A3)