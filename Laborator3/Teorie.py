
#Functii
def function_name(x):
    return sum(x)

print(function_name([1,2,3]))

#*args si **kwargs

def my_fun(arg1,*argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv:", arg)
my_fun('Hello','Welcome','to','Python')

def my_func(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key,value))
my_func(first = 'B',mid='to',last='C')

fib = lambda n: n if n <= 1 else fib(n - 1) + fib(n - 2)
result = fib(10)
print(result)

dublu = lambda x: x * 2
print(dublu(5))

# Functia map()

def addition(n):
    return n+n

numbers=(1,2,3,4)
result = map(addition,numbers)
print(list(result))

#Functia filter()

def fun(variable):
    letters=['a','e','i','o','u']
    if variable in letters:
        return True
    else:
        return False

sequence = ['g','e','e','j','k','s','p','r']

filtered=filter(fun,sequence)
for s in filtered:
        print(s)

#Functia reduce()
import functools
lis = [1,3,5,6,2]

print("The sum of the list element is ",end="")
print(functools.reduce(lambda a,b:a+b,lis))

print("The maximum element of the list is: ",end="")
print(functools.reduce(lambda a,b:a if a>b else b,lis))

#Functia zip()

names=['Andra','Cristina','Marius']
ages=[21,23,22]

for i,(name,age) in enumerate(zip(names,ages)):
    print(i,name,age)

#Comprehensions

output = [i+j for i in range(3) for j in range(3)]
print(output)

output=[]
for i in range(3):
    for j in range(3):
        output.append(i+j)
print (output)