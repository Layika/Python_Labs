#!/usr/bin/python3.5

import random
import sys

# Write a function that checks if its argument is a prime number
def is_prime(n):
    if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               return False
       else: return True
    else: return True

# Create a dictionary of 50 elements with keys as numbers from 0 to 100 and values as True/False based on if
# number is prime or not. If a key already exist in dict then do nothing
numbers = {}
while len(numbers) < 50:
    k=random.randint(0,100)
    numbers.setdefault(k, is_prime(k))

# Create a list of 100 numbers in range from 0-20
# And then create two dictionaties, of even and odd numbers and their indexes in list
nums_list = [random.randint(0,20) for el in range(100)]
odds = {}
evens = {}

for num,val in enumerate(nums_list):
    if val%2:
        odds.setdefault(val, []).append(num)
    else:
        evens.setdefault(val, []).append(num)

# Create a dict with keys from odds and if any of their indexes can be divided by 3 then as value us that list
# If not put there a tuple with  min index and max index
new_dict = {el:idx if [i for i in idx if not i%3] else (idx[0], idx[-1]) for el,idx in odds.items()}

# Create a dict with as many keys as argument passed to this program says, values have to be between 2 and 15
if len(sys.argv) < 2:
    print("Usage: ./lab3.py num")
    sys.exit()

dict_of_num = {i:random.randint(2,15) for i in range(0, num)}

# Create a list from that dict: both keys and values have to be list's elements but they have to be switched
list_from_dict = [(y, x) for x,y in dict_of_num.items()]

# Create a dict from dict_of_num with keys and values switched
switched_dict = {y:x for x,y in dict_of_num.items()}

# Create a list of 100 random numbers between 0 and 11
list_100 = [random.randint(0,11) for i in range(100)]
# And then create a dict with keys 0-11 and lists of indexes of these keys in the list as values
dict_100={}
for el in list_100:
    dict_100.setdefault(el,[]).append(list_100.index(el, dict_100.get(el)[-1]+1 if dict_100[el] else 0))


# Create two dicts wirh 10 values between 1 and 100
first_dict = {i:random.randint(1,100) for i in range(10)}
second_dict = {i:random.randint(1,100) for i in range(10)}

# And then switch values and keys
first_dict = {y:x for x,y in first_dict.items()}
second_dict = {y:x for x,y in second_dict.items()}

# Create a dict of elements that are present in both dicts, values have to be tuples of values from first and second dict
res_dict = {i:(first_dict[i], second_dict[i]) for i in first_dict if i in second_dict}
