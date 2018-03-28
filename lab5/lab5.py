#!/usr/bin/python3.5

from time import time
from sys import version, exit
import random
from functools import reduce
from math import sqrt

points = 10**6
def countPi(points):
    return 4 * sum(list(filter(lambda x: random.random()**2 + random.random()**2 < 1, (1 for i in range(points))))) / points
countPi(points)

powt=1000
N=10000

def forStatement():
    l = []
    for i in range(N):
        l.append(i**2)

def listComprehension():
    l = [i**2 for i in range(N)]

def mapFunction():
    l = list(map(lambda i: i**2, range(N)))

def generatorExpression():
    l = list((i**2 for i in range(N)))

def tester(fun):
    start = time()
    for i in range(powt):
        fun()
    end = time()
    return end - start

'''
z generatorami jest szybciej

2.7.12 (default, Dec  4 2017, 14:50:18)
[GCC 5.4.0 20160609]
('forStatement        ', '=>', 1.2386870384216309)
('listComprehension   ', '=>', 0.8681979179382324)
('mapFunction         ', '=>', 1.367901086807251)
('generatorExpression ', '=>', 1.0180838108062744)

3.5.2 (default, Nov 23 2017, 16:37:01)
[GCC 5.4.0 20160609]
forStatement         => 3.9929866790771484
listComprehension    => 3.3456227779388428
mapFunction          => 4.219467401504517
generatorExpression  => 3.657472848892212
'''
print(version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
matrix2 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

def max(x):
    biggest = x[0]
    for i in x:
        if i > biggest:
            biggest = i
    return biggest

def biggestInRow(matrix):
    return list(map(max, matrix))

def biggestInCol(matrix):
    return list(map(max, zip(*matrix)))

def addMatrix(matrix1, matrix2s):
    pass
    #return zip(matrix1, matrix2)


def countWeirdStuff(x=[], y=[]):
    if not len(x) or not len(y):
        sys.exit(-1)

    xAvg = sum(x)/len(x)
    yAvg = sum(y)/len(y)

    xList = []
    for i in x:
        xList.append(i)
        xList.append(xAvg)

    D = reduce(lambda x, y: (x-y)**2, xList)

    yxList = []
    for i in range(len(y)):
        yxList.append(y[i])
        yxList.append(x[i])

    a = 1/D * reduce(lambda y, x: y*(x-xAvg), yxList)

    b = yAvg - a*xAvg

    n = len(x)
    yDelta = sqrt( reduce(lambda y, x: y*(a*x+b), yxList) / (n-2) )

    aDelta = yDelta/sqrt(D)

    bDelta = yDelta * sqrt(1/n * xAvg**2/D)

    return (D, a, b, yDelta, aDelta, bDelta)
