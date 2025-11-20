#IF23 Вершинин ИСП111
X1 = int(input())
X2 = int(input())
X3 = int(input())
Y1 = int(input())
Y2 = int(input())
Y3 = int(input())
X4 = X1 if X2 == X3 else (X2 if X1 == X3 else X3)
Y4 = Y1 if Y2 == Y3 else (Y2 if Y1 == Y3 else Y3)