#IF21 Вершинин ИСП111
X = int(input())
Y = int(input())
if X == 0 and Y == 0:
    print(0)
elif X == 0 and Y != 0:
    print(1)
elif X != 0 and Y == 0:
    print(2)
else:
    print(3)