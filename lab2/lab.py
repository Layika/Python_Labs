#!/usr/bin/python3.5

import sys

# If no arguments for the program are given then print how to call it and exit
if len(sys.argv) < 2:
    print("Usage: ./lab.py <string1> [string2] [string3] ...")
    sys.exit()

# Join all arguments given by user in a string
string = ' '.join(sys.argv[1:])

# Create lists for lowercase letters, uppercase letter, numbers and other characters from that string
small_letters = [el for el in string if el.islower()]
big_letters = [el for el in string if el.isupper()]
numbers = [el for el in string if el.isnumeric()]
other = [el for el in string if not el.islower() and not el.isupper() and not el.isnumeric()]

# Create a new list of not characters from small_letters but remove duplicates
def remove_duplicates(lst):
    newlist = []
    for char in lst:
       if char not in newlist:
           newlist.append(char)
    return newlist

not_doubled = remove_duplicates(small_letters)

# Create a list of tuples containing a character from not_doubled and count of it's occurences in small_letters
counted = [(el, small_letters.count(el)) for el in not_doubled]

# Sort that list by number of occurences
counted = sorted(counted, key=lambda x: x[1])

# Count vovels and consonants in string (name them a nd b because will be needed in counting ax+b)
a = sum(1 for i in string if i.casefold() in 'aeiou')
b = len(string) - len(numbers) - len(other) - a

# Create a list of tuples containing numbers from numbers list and value of function
num_and_val = [(int(el), a*int(el)+b) for el in numbers]

# Count value of a and b using a method of least squares
avg_x = sum(el[0] for el in num_and_val)/len(num_and_val)
avg_y = sum(el[1] for el in num_and_val)/len(num_and_val)
D = sum((int(el)-avg_x)**2 for el in numbers)
check_a = (1.0/D) * sum(y*(x-avg_x) for x,y in num_and_val)
check_b = avg_y - check_a*avg_x
