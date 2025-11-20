#IF5 Вершинин ИСП111
a = int(input())
b = int(input())
c = int(input())
if a > 0 and b > 0 and c > 0:
    print(3)
    print(0)
elif (a > 0 and b > 0 or a > 0 and c > 0 or b > 0 and c > 0) and not(a > 0 and b > 0 and c > 0):
    print(2)
    print(1)
elif (a > 0 and b < 0 and c < 0) or (a < 0 and b > 0 and c < 0) or (a < 0 and b < 0 and c > 0):
    print(1)
    print(2)
else:
    print(0)
    print(3)