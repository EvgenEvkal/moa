#IF20 Вершинин ИСП111
A = float(input())
B = float(input())
C = float(input())
if abs(B - A) < abs(C - A):
    print("A")
    print(abs(B - A))
elif abs(B - A) > abs(C - A):
    print("B")
    print(abs(C - A))
else:
    print("И А и B")
    print(abs(C - A))