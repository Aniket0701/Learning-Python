
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


name = input('please write your name')

print(len(name))

quote = 'String'

print(quote.count('$'))

List1 = [1 , 2 , 2,'Hello', True]

print(type(List1))
print(List1)
print(len(List1))

Thislist = list(('apple', 'Banana', 'Grapes'))

print(Thislist)

#Access List Items

List1 = [1 , 2 , 2,'Hello', True]

print(List1[-1])

#Range of Indexes

List2 = ['Apple','Banana','Grapes','Orange','Melon', 'Mango']

print(List2[-3:])

#find in the list
Basket = ['Apple','Banana','Grapes','Orange','Melon', 'Mango']
if 'Apple' in Basket:
    print('Apple is in the Basket')
else:
    print('No apple in the Basket')

#changes  in the list

Fruits = ['Apple','Banana','Grapes','Orange','Melon', 'Mango']

Fruits[4] = 'Watermelon'
print(Fruits)

#changes in the range

Family = ['Aniket','Namrata','Mummy','Sonal']
Family[1:] = 'Chuku','Mom','sister'
print(Family)

Basket = ['Apple','Banana','Grapes','Orange','Melon', 'Mango']
Basket[-2:-1] ='Watermelon' , 'Muskmelon'
print(Basket)

#insert Items

list = ['Apple', 'Banana' ,'Grapes']
list.insert(1,'Watermeelon')
print(list)

#Append
Garage = ['Yamaha R1', 'BMW S1000RR', 'Porshe 911 GT3 RS', 'BMW M4 Competition']
Garage.append('Mercedes Maybach')
print(Garage)

#insert is for specific index
Garage = ['Yamaha R1', 'BMW S1000RR', 'Porshe 911 GT3 RS', 'BMW M4 Competition']
Garage.insert(3,'Mercedes Maybach')
print(Garage)

# Add items from 1 list to another list
Garage = ['Yamaha R1', 'BMW S1000RR', 'Porshe 911 GT3 RS', 'BMW M4 Competition']
Showroom = ['Toyota Land Crusier','Mercedes Maybach']
Garage.extend(Showroom)
print(Garage)

#Remove items from a list
Garage = ['Yamaha R1', 'BMW S1000RR', 'Porshe 911 GT3 RS', 'BMW M4 Competition']
Garage.remove('Yamaha R1')
print(Garage)

Basket = ['Apple','Banana','Grapes','Orange','Melon', 'Mango', 'Grapes']
Basket.remove('Grapes')
print(Basket)

#Remove Specified index

Basket = ['Apple','Banana','Grapes','Orange','Melon', 'Mango']
Basket.pop(0)
print(Basket)

#empty function will delete the last item in the list
Basket = ['Apple','Banana','Grapes','Orange','Melon', 'Mango']
Basket.pop()
print(Basket)

#Del function - which also remove from specified index from the list.

Basket = ['Apple','Banana','Grapes','Orange','Melon', 'Mango']
del Basket[0]
print(Basket)

Garage = ['Yamaha R1', 'BMW S1000RR', 'Porshe 911 GT3 RS', 'BMW M4 Competition']
del Garage
print(Garage)

#clear the list

Garage = ['Yamaha R1', 'BMW S1000RR', 'Porshe 911 GT3 RS', 'BMW M4 Competition']
Garage.clear()
print(Garage)

# For loop through a list
Garage = ['Yamaha R1', 'BMW S1000RR', 'Porshe 911 GT3 RS', 'BMW M4 Competition']
for X in Garage:
    print(X)

Garage = ['Yamaha R1', 'BMW S1000RR', 'Porshe 911 GT3 RS', 'BMW M4 Competition']
for i in range(len(Garage)):
    print(Garage[i])

#While loop
Garage = ['Yamaha R1', 'BMW S1000RR', 'Porshe 911 GT3 RS', 'BMW M4 Competition']
i = 0
while i < len(Garage):
    print(Garage[i])
    i = i+1

#Looping using List comprehension

Garage = ['Yamaha R1', 'BMW S1000RR', 'Porshe 911 GT3 RS', 'BMW M4 Competition']
[print(x) for x in Garage]

## List comprehension
#1
Showroom = ['Yamaha R1', 'BMW S1000RR', 'Porshe 911 GT3 RS', 'BMW M4 Competition']
newlist = []
for x in Showroom:
    if 'Y' in x:
        newlist.append(x)
print(newlist)

#2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#3
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != 'apple']
print(newlist)

#4
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in range(10) if x < 5]
print(newlist)

#5
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

#6
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != 'banana' else 'orange'for x in fruits]
print(newlist)

# Sort List
Showroom = ['Yamaha R1', 'BMW S1000RR', 'Porshe 911 GT3 RS', 'BMW M4 Competition']
Showroom.sort()
print(Showroom)

numbers = [12,45,15,60,100]
numbers.sort()
print(numbers)

#Sort Desc
numbers = [12,45,15,60,100]
numbers.sort(reverse = True)
print(numbers)

# Practice questions on conditional statement

# 1. Find the number is odd or even.

number = int(input('Write the number'))

if (number % 2 == 0):
    print('it\'s an even number')
else:
    print('it\'s odd number')

# 2 greatest number
A = int(input('write the first number'))
B = int(input('write the second number'))
C = int(input('write the third number'))

if (A > B and A > C):
    print('A is greatest number')
elif (B > A and B > C):
    print('B is the greatest number')
else:
    print('c is the greatest number')

#3 multiple of 7 or not

number = int(input('please write the number'))

if (number % 7 == 0):
    print('yes this number is a multiple of 7')
else:
    print('No this number is not a multiple of 7')

#Practice Questions on list

#1. Ask user to enter three fav movies & store them in a list

movies = []
mov1 = input('Please mention your First fav movie')
mov2 = input('Please mention your second fav movie')
mov3 = input('Please mention your Third fav movie')

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)