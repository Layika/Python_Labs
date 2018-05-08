import random
import math
import glob
import os

def check(x, y, z):
    if x<=0 or y<=0 or z<=0 or x>=y:
        raise ValueError

    else:
        numbers = [random.randint(x, y) for i in range(z)]
        print(numbers)
        odds = 0
        evens = 0
        for num in numbers:
            if num%2: odds += 1
            else: evens += 1

        if odds == 0: raise ZeroDivisionError
        else: return evens/odds

try:
    check(0,2,3)
except ValueError: print("Invalid arguments!")
except ZeroDivisionError: print("Division by zero!")

try:
    check(3,1,5)
except ValueError: print("Invalid arguments!")
except ZeroDivisionError: print("Division by zero!")


def findRoots(func, x=0.0, step=1e3, prec=1e-7):
    test = lambda x: func(x) > 0

    begin, end = test(x), test(x + step)
    assert begin != end

    while abs(step) > prec:
        step *= 0.5
        if test(x + step) is not end: x += step
    print(x)
    return x


# x+1 [-2,0]
try: findRoots(lambda x: x+1, x=-2, step=3)
except AssertionError: print("Can't find roots there!")

# x+1 [1, 2],
try: findRoots(lambda x: x+1, x=1, step=2)
except AssertionError: print("Can't find roots there!")

# (x-2)*(x-2)/(x-1)-2 [0, 2]
try: findRoots(lambda x: (x-2)*(x-2)/(x-1)-2, x=0, step=3)
except AssertionError: print("Can't find roots there!")

# (x-2)*(x-2)/(x-1)-2 [4, 6]
try: findRoots(lambda x: (x-2)*(x-2)/(x-1)-2, x=4, step=3)
except AssertionError: print("Can't find roots there!")


def pythagorean(lst):
    div=0
    if len(lst)%3 == 0: div=3
    if len(lst)%4 == 0: div=4
    if not div: raise ValueError

    elements = [lst[x:x+div] for x in xrange(0, len(lst), div)]
    for i in elements:
        correct=False
        assert max(i) == i[-1]

        if div==3:
            if i[0]**2 + i[1]**2 == i[2]**2: correct=True
        else:
            if i[0]**2 + i[1]**2 + i[2]**2 == i[3]**2: correct=True

        if correct:
            odds = 0
            evens = 0
            for num in i:
                if num%2: odds += 1
                else: evens += 1
            print(i, evens, odds)


l=[1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,
12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,
21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,
23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29,2]
try: pythagorean(l)
except ValueError: print("Bad length of list!")
except AssertionError: print("Last element of sublist is not biggest!")

l=[1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,
12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,
21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,
23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29]
try: pythagorean(l)
except ValueError: print("Bad length of list!")
except AssertionError: print("Last element of sublist is not biggest!")

l=[3,4,5,5,12,13,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17]
try: pythagorean(l)
except ValueError: print("Bad length of list!")
except AssertionError: print("Last element of sublist is not biggest!")

l=[3,4,5,5,13,12,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17]
try: pythagorean(l)
except ValueError: print("Bad length of list!")
except AssertionError: print("Last element of sublist is not biggest!")


def aver(fileName):
    with open(fileName) as f:

        lines = f.readlines()
        if len(lines) == 0: raise ZeroDivisionError

        numericalValues=True
        sumCols=0

        for i in lines:
            i = i.strip('\n')
            i = i.split()

            for char in i:
                if not char.isdigit(): raise ValueError

            assert len(i) == 2

            sumCols += float(i[0])
            sumCols += float(i[1])

        avg = sumCols/len(lines)

        scriptDir = os.path.dirname(os.path.abspath(__file__))
        filePath = os.path.join(scriptDir, fileName+":"+str(avg))
        f = open(filePath, 'w+')
        f.write(str(avg))
        f.close()


for i in glob.glob('*.dat'):
    try: aver(i)
    except ZeroDivisionError: print("No lines in file!")
    except AssertionError: print("Bad columns!")
    except ValueError: print("Not numerical values in file!")
