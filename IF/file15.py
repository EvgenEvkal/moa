#IF15 Вершинин ИСП111
a = int(input())
b = int(input())
c = int(input())
if b > a < c:
    print(b + c)
elif a > b < c:
    print(a + c)
elif a > c < b:
    print(a + b)