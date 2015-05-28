def regressionLine(x, y):
    sumSquareX = sum([n**2 for n in x])
    sumSquareY = sum([n**2 for n in y])
    sumX = sum(x)
    sumY = sum(y)
    sumXY = sum([X*Y for X,Y in zip(x,y)])
    a = ((sumSquareX*sumY) - (sumX*sumXY)) / float(((len(x) * sumSquareX) - sumX**2))
    b = ((len(x)*sumXY) - (sumX*sumY)) / float(((len(x)*sumSquareX) - sumX**2))
    a = round(a,4)
    b = round(b,4)
    return a,b
    


print(regressionLine([25,30,35,40,45,50], [78,70,65,58,48,42]))
#(114.381, -1.4457)
#a =  [(Σx²)(Σy) - (Σx)(Σxy)]  /  [n(Σx²) - (Σx)²]
#b =  [n(Σxy) - (Σx)(Σy)] / [n(Σx²) - (Σx)²]