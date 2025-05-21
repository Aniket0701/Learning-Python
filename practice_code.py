
a = 'Hello_World'
print (a)

# First Code
print("hello, World!")

# checking Version
import sys
print(sys.version)

# Variables & it's Type
a = 1
b = 2.0
c = True
d = 'Hello'

print(type(a), type(b), type(c), type(d))

x,y,z = 'Orange', 'apple','Banana'
print(x,y,z)

x = y = z = 'Apple'
print(x,y,z)

Fruits = ['Apple','Mango','Grapes']
x,y,z = Fruits
print(x,y,z)

x = 'Python is Awesome'
print(x)

x = 'python '
y = 'is '
z = 'Awesome'

print(x+y+z)

x= 5
y = 10
print(x+y)

x = 5
y = 'john'

print(x ,y)

x = 'awesome'

def myfunc():
    print('python is ' + x)

myfunc()

x = 50
y = 100
z = 150

def MyFunction():
    print(x+y+z)

MyFunction()

x = 'Awesome'

def myfunc():
    global x
    x = ' fantastic'
    print('python is' + x)

myfunc()

print ('python is' + x)

# Numbers 
x = range(6)
print(type(x))


z = 1
a =float(z)

print(type(z))
print(type(a))

import random
print(random.randrange(1,10))

#Casting
x = int(25.10)
y = float(10)
z = str(1000)

print(x , y , z)

# String

print('Hello World')

a = 'Hello, World'
print(a[:5])

for x in 'banana':# String in loops
    print(x)

a = "hello"
print(len(a)) # Length

# IN
TXT = 'The best thing in life are free'

print('free' in TXT)

#Not In

txt = 'The best thing in life are free!'

print('expensive' not in txt)

# String Slicing
b = 'Hello, World'
print(b[2:5])

A = 'Hello World'
print(A[-5:-2])

#Modify
a = "I need to learn python"
print(a.upper())

b = 'I NEED TO LEARN SQL'
print(b.lower())

C = '  Welcome to INDIA '
print(C.strip())

d = 'i need a job in data science'
print(d.replace('i','I')) 

E = 'Life is tough'
print(E.split(' '))

# concatenation

a = 'hello'
b = 'World'
C = (a+ ' ' +b)
print(C)

# Format

Age = 23
txt = f'My name is Aniket, I am {Age}'
print(txt)

price = 100
txt = f'Mango is {price} rupess per kg in the Market'
print(txt)

price = 45
txt = f'the price is {price:.2f} dollars'
print(txt)

txt = f'The price is {20*59} dollars'
print(txt)

TXT = 'We are the so-called \n"Vikings" from the north.'
print(TXT)

name = 'aniket Shukla'
print(name.capitalize())

a = int(input('Please assign 1 number'))
b = int(input('please assign 2 number'))

if a>b:
    print('a is greater than b')
else:
    print('b is greater than a')

# Bool 
print(bool('aniket'))
print(bool(12))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction():
    return True

if myFunction():
    print('YES')
else:
    print('NO')

x = 200
print(isinstance(x, int))

# Arithmetic operator

a = 50
b = 25
print(a+b)
print(a-b)
print(a/b)
print(a%b)
print(a*b)
print(a//b)
print(a**b)

a = 100
b = 10
print (a>b)

# Practice Program
a = int(input('Please write first number'))
b = int(input('Please write Second number'))

Sum = a+b
print(Sum)

# practice Program
Sides = float(input('Please mention the side of a square'))

Area = Sides * Sides
print(Area)

# third practice program
a = float(input('Please write first number'))
b = float(input('Please write Second number'))

average = (a+b)/2

print(f'{average} average of Two numbers')

# Fourth program
a = int(input('Please write first number'))
b = int(input('Please write Second number'))

if (a >= b):
    print('True')
else:
    print('False')