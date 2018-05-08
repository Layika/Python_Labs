import numpy as np


def poczatkowe(nazwa_pliku, n):
    with open(nazwa_pliku) as f:
        lista_wierszy = [f.readline() for i in range(n)]
    return lista_wierszy

print(poczatkowe("notes", 3))
print("\n")

def koncowe(nazwa_pliku, n):
    with open(nazwa_pliku) as f:
        lista_wierszy = f.readlines()[:-n]
    return lista_wierszy

print(koncowe("notes", 4))
print("\n")

def co_n_wiersz(nazwa_pliku, n):
    with open(nazwa_pliku) as f:
        lista_wierszy = [i for i in f.readlines()[::n]]
    return lista_wierszy

print((co_n_wiersz("test", 3)))
print("\n")

def co_n_slowo(nazwa_pliku, n):
    with open(nazwa_pliku) as f:
        lista_slow = [i.split(' ')[n] for i in f.readlines()]
    return lista_slow

print(co_n_slowo("test_slowa", 2))
print("\n")

def co_n_znak(nazwa_pliku, n):
    with open(nazwa_pliku) as f:
        lista_slow = [i[n] for i in f.readlines()]

print(co_n_znak("test_slowa", 3))

def print_count_replace(file_name, to_replace, replace_by):
    counter = 0
    with open(file_name) as f:
        for line in f:
            if line.startswith(to_replace): print(line)
            counter += line.count(to_replace)
            print("before = %s" % line)
            line = line.replace(to_replace, replace_by)
            print("after = %s" % line)
    print("counter = %d" % counter)

print_count_replace('test_replace', 'aaa', 'xyz')
