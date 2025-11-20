#IF19 Вершинин ИСП111
A = int(input())
B = int(input())
C = int(input())
D = int(input())
if A != B and B == C == D:
    print(1)
elif B != A and A == C == D:
    print(2)
elif C != A and A == B == D:
    print(3)
elif D != A and A == B == C:
    print(4)