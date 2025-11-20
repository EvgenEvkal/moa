#IF13 Вершинин ИСП111
a = int(input())
b = int(input())
c = int(input())
if b > a < c:
    if a < b > c:
        print(c)
    else:
        print(b)
elif a > b < c:
    if b < a > c:
        print(c)
    else:
        print(a)
elif b > c < a:
    if c < a > b:
        print(b)
    else:
        print(a)