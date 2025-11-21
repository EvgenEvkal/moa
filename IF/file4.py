#IF4 Вершинин ИСП111
a,b,c = int(input()),int(input()),int(input())
if a > 0 and b > 0 and c > 0:
    print(3)
elif (a and b) > 0 or (b and c) > 0 or (c and a) > 0:
    print(2)
elif a > 0 or b > 0 or c > 0:
    print(1)
else:
    print(0)