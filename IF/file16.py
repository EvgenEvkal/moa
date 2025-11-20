#IF16 Вершинин ИСП111
A = float(input())
B = float(input())
C = float(input())
if A < B and B < C:
    print(A*2)
    print(B*2)
    print(C*2)
else:
    print(A*-1)
    print(B*-1)
    print(C*-1)