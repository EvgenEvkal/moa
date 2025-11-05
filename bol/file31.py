#Boolean31 Вершинин ИСП111
a = int(input())
b = int(input())
c = int(input()) 
print((a == b or b == c or a == c) and not(a == b == c))