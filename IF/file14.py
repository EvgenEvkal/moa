#IF14 Вершинин ИСП111
a = int(input())
b = int(input())
c = int(input())
if a > b < c:
    print(b)
    if b < a > c:
        print(a)
    else:
        print(c)
elif a > c < b:
    print(c)
    if c < a > b:
        print(a)
    else:
        print(b)
elif c > a < b:
    print(a)
    if a < c > b:
        print(c)
    else:
        print(b)