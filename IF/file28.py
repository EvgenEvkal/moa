#IF28 Вершинин ИСП111
x = int(input())
print(366 if x % 4 == 0 and (x % 100 != 0 or x % 400 == 0) else 355)