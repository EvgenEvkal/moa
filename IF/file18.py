#IF18 Вершинин ИСП111
A = int(input())
B = int(input())
C = int(input())
if A != B and B == C:
    print(1)
elif B != A and A == C:
    print(2)
elif C != A and A == B:
    print(3)