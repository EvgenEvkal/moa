#IF9 Вершинин ИСП111
A = float(input())
B = float(input())
if A > B: A,B = B,A; print(A); print(B)
else: print(A); print(B) if B > A else None