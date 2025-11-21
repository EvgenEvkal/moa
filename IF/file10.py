#IF10 Вершинин ИСП111
A = int(input())
B = int(input())
if A != B:
    A,B = A+B,A+B
else:
    A,B = 0,0
print(A)
print(B)