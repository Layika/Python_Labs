import fibonacci
import newton
# Divide fibonacci into two classes and see what it does
import fibonacciSecond
import randomNum
import math
import random

# 1
print("Fibonacci one class")
f = fibonacci.Fibonacci(10)
for i in f:
    for j in f:
        print(i, j)


print("\n\nFibonacci two classes")
f = fibonacciSecond.FibonacciIter()
for i in f:
    for j in f:
        print(i, j)


# 2
print("\n\nNewton")
def f(x):
    return math.sin(x)-(0.5*x)**2
x0 = 1.5
eps = 10**-5

for i in newton.Newton(f, x0, eps):
    print(i)


print("\n\nRandom numbers iterator")
m = 2**31-1
a = 7**5
c = 0
x0 = 1
maxNum = 10**5

squareIter = [0] * 10
sguareGen = [0] * 10

r = randomNum.RandomNum(m, a, c, x0)
for i in range(maxNum):
    x = next(r)/m
    y = next(r)/m

    xP = random.random()
    yP = random.random()

    for idx in range(1, len(squareIter)+1):
        if x <= idx*0.1 and y <= idx*0.1:
            squareIter[idx-1] += 1
        if xP <= idx*0.1 and yP <= idx*0.1:
            sguareGen[idx-1] += 1

print(squareIter)
print("\nPython random numbers")
print(sguareGen)
