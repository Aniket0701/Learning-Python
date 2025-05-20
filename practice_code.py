
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