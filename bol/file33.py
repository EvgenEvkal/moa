#Boolean33 Вершинин ИСП111
a = int(input())
b = int(input())
c = int(input())
s = a + b + c
max_st = max(a,b,c)
print(max_st - (s - max_st) < 0)