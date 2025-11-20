#IF11 Вершинин ИСП111
A = int(input())
B = int(input())
if A != B:
    if A > B:
        A,B = A,A
    else:
        A,B = B,B
else:
    A,B = 0,0
print(A)
print(B)