#Tipuri de date

mesaj = "Laborator AI"
print('*' * (len(mesaj) + 4))
print('* ' + mesaj + ' *')
print('*' * (len(mesaj) + 4))

#Numeric

print(type(1))
print(type(-10))
print(type(0))
print(type(0.0))
print(type(2.2))
print(type(4E2))

print(10+3)
print(10-3)
print(10*3)
print(10**3)
print(10/3)
print(10//3)
print(10%3)

print(pow(5,2))
print(abs(-50))
print(round(5.46))
print(round(5.468,2))
print(bin(512))
print(hex(512))

age = input("How old are you?")
age = int(age)
print(age)

pi = input("What is the value of pi?")
pi = float(pi)

#2.Strings
print(type('Hellllooooo'))
print('I\'m thirsty')
print("I'm thirsty")
print("\n")
print("\t")

print('Hey you!'[4])
name = 'John Doe'
print(name[2])
print(name[:])
print(name[1:])
print(name[:1])
print(name[-1])
print(name[::1])
print(name[::-1])
print(name[0:7:2])

print('Hi there ' + 'Timmy')
print('*'*10)

print(len('turtle'))
print(' I am alone '.strip())
print('On a island'.strip('d'))
print('but life is good'.split())
print('Help me'.replace('me', 'you'))
print('Need to make fire'.startswith('Need'))
print('and cook rice'.endswith('rice'))
print('bye bye'.index('e'))
print('still there?'.upper())
print('HELLO?!'.lower())
print('ok, I am done'.capitalize())
print('oh hi there'.find('i'))
print('oh hi there'.count('e'))

name1 = 'Andrei'
name2 = 'Sunny'

print(f'Hello there {name1} and {name2}')
print('Hello there {} and {}'.format(name1, name2))
print('Hello there %s and %s'%(name1, name2))

word = 'reviver'
p = bool(word.find(word[::-1]) + 1)
print(p)

#3.Boolean

print(bool(True))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(''))
print(bool(range(0)))
print(bool(set()))

#4.List

my_list = [1, 2, '3', True]
print(len(my_list))
print(my_list.index('3'))
print(my_list.count(2))

print(my_list[3])
print(my_list[1:])
print(my_list[:1])
print(my_list[-1])
print(my_list[::1])
print(my_list[::-1])
print(my_list[0:3:2])

print(my_list * 2)
print(my_list + [100])
my_list.append(100)
print(my_list)
my_list.extend([100, 200])
print(my_list)
my_list.insert(2, '!!!')
print(my_list)
print(' '.join(['Hello' , 'There']))

basket = ['apples', 'pears', 'oranges']
new_baschet = basket.copy()
new_baschet2 = basket[:]

print(new_baschet)
print(new_baschet2)

print([1,2,3].pop())
print([1,2,3].pop(1))
print([1,2,3].remove(2))
print([1,2,3].clear())

lista = [1,2,5,3]
lista.sort()
print(lista)

lista = [1,2,5,3]
lista.sort(reverse=True)
print(lista)

lst = [1,2,5,3]
lst.reverse()
print(lst)
print(sorted([1,2,5,3]))
print(list(reversed([1,2,5,3])))

print(1 in [1,2,5,3])
print(min([1,2,3,4,5]))
print(max([1,2,3,4,5]))
print(sum([1,2,3,4,5]))

mList = [63, 21, 30, 14, 35, 26, 77, 18, 49, 10]
first, *x, last = mList
print(first)
print(last)

with open(r"C:\Users\andra\OneDrive\Desktop\Facultate\Anul 3\Semestrul 2\Inteligenta artificiala\Laborator\Inteligenta Artificiala\Laborator1\myfile.txt") as f:
    lines = [line.strip() for line in f]
print(lines)

#5.Dictionary

my_dict = {'name': 'John Doe', 'age': 25, 'magic_power': False}
print(my_dict['name'])
print(len(my_dict))
print(list(my_dict.keys()))
print(list(my_dict.values()))
print(list(my_dict.items()))

my_dict['favourite_snack'] = 'Grapes'

print(my_dict.get('age'))
print(my_dict.get('ages', 0))

del my_dict['name']
my_dict.pop('name', None)

#6.Tuple

my_tuple = ('apple','grapes', 'mango', 'grapes')
apple, grapes, mango, grapes = my_tuple

print(len(my_tuple))
print(my_tuple[2])
print(my_tuple[-1])

# my_tuple[1] = 'donuts'- Tuplul este imutabil
# my_tuple.append('candy') - Tuplul nu are append

print(my_tuple.index('grapes'))
print(my_tuple.count('grapes'))

#7.Set

my_set = set()
my_set.add(1)
my_set.add(100)
my_set.add(100)
print(my_set)

new_list = [1,2,3,3,3,4,4,5,6,1]
new_set = set(new_list)
print(new_set)
my_set.remove(100)
print(my_set)
my_set.discard(100)
print(my_set)
my_set.clear()
print(my_set)
new_set = {1,2,3}.copy()

set1 = {1,2,3}
set2 = {3,4,5}
set3 = set1.union(set2)
set4 = set1.intersection(set2)
set5= set1.difference(set2)
set6 = set1.symmetric_difference(set2)
print(set3)
print(set4)
print(set5)
print(set6)
print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.isdisjoint(set2))


#8.None

print(type(None))
a = None
print(a)