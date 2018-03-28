#!/usr/bin/python3.5
import random
import sys

# Make a dict with 20 random numbers between 0-1 as keys and a value of 2*key+3 formula as values
# Both have to be written with 3 digits after dot
def makeDict(x):
    s = {}
    for i in range(20):
        x = random.random()
        s.setdefault(str("%.3f" % x), "%.3f" % eval('2*{:.3g}+3'.format(x)))

# Write a function that takes variable amount of arguments and return a list of elements that are present in all of these lists
def returnCommon(*listOfLists):
    commonList = []
    for i in listOfLists[0]:
        commonList.append(i)

    for lst in listOfLists[1:]:
        for elem in commonList:
            if elem not in lst:
                commonList.remove(elem)

# Write a function that takes two lists and an optional True/False (default as True)
# Return a list of tuples of elements in these lists on the same indexes
# If vale == True choose the length of result list as length of shorter of the lists from arguments
# If its False then fill tuples with None when it comes to adding elements from shorter list but the list is shorter
def returnIndexes(first=[], second=[], value=True):
    if value: return [(first[i], second[i]) for i in range(len(first) if len(first) < len(second) else len(second))]
    else: return [(first[i] if i < len(first) else None, second[i] if i < len(second) else None) for i in range(len(first) if len(first) > len(second) else len(second))]

# Write a function for comparing to numbers
# And then write a function that would take it as an argument and return it's result
def cmp(x, y):
    if x > y: return x
    else: return y

def compareValues(fun, x, y):
    return eval(str(fun(x,y)))

print(compareValues(cmp, 1, 2))

# Write a function for changing coins
def makeCoins(x, nominals=(10,5,2)):
    listOfCoins = []
    while x > 0:
        for coin in nominals:
            if x >= coin:
                count = x//coin
                for i in range(count): listOfCoins.append(coin)
                x = x % coin
            elif coin == nominals[-1]:
                print("Cannot divide!")
                return []
    return listOfCoins

# Write a function that would find a given number using bisection method
# If default argument is equal to 'r' then middle element has to be literally in the middle
# If not then choose a random number for this
def findValue(toFind, start, end, way='r'):
    if toFind > end or toFind < start:
        print("Too small or too big numer!")
        sys.exit()

    else:
        found = False

        while not found:
            divide = start + (end-start)//2 if way == 'r' else random.randint(start, end)
            if toFind == divide: found = True
            if toFind > divide: start = divide
            else: end = divide

        print("Found!")
        return divide

print(findValue(13, 10, 20))
