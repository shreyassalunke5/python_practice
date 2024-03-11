print("hello")
print("""hihoware you""")
print("hi\n are\n you")

age = int(input("enter age - "))
print(age)
ht = float(input("enter height - " ))
print(ht)

b= int("5")
c = 6
d = b+c
print(d)
print(type(b))

a= 5
b = 6
print (a)
print (b)
a, b = b, a
print (a)
print (b)

#print(bin(10))
#print(bin(8))
#print(bin(10 and 8))
#print(bin(10 or 8))
#print(10 and 8)
#print(10 ^8)
#print(10>>1)
#print(bin(10>>1))
#print(bin(10>>2))
#print(bin(10>>3))
#print(bin(10<<3))


## if elif else ##

flavour = "mo"
if flavour =="vanila":
    print("not good")
elif flavour=="mango":
   print("good")
else:
    print("fine")

## nested if ##

marks = 97
if marks>=85:
    print ("good")
    if marks>=90:
        print("excellent")
else:

     print("bad")

## one liner ##

marks = 95
print("good ") if marks >=90 else print("not bad")

l= int(input("enter number: "))
print("positive") if l>=0  else print("negative")

## finding area ##

print("find area")
print("""for circle enter 1
#for square enter 2
#for triangle enter 3""")
value = int(input("enter the value: "))
if value ==1:
    r = int(input("enter radius: "))
    area1 = 3.14 * r * r
    print("area of circle is: ",area1)
elif value ==2:
    s = int(input("enter side: "))
    area2 = s**2
    print("area of square is: ", area2)
elif value == 3:
    h = int(input("enter the height: "))
    b = int(input("enter the breadth: "))
    area3 = h*0.5*b
    print("area of triangle is: ", area3)
else:
    print("please enter valid input")

## in ##

o = input("enter alphabet: ")
if o in "aeiou":
    print("vowel")
else:
    print("consonant")

## for loop ##

for i in range(1,5,2):
   print("hi")

n=6
for i in range(1,5):
    print(n*i)

## while loop ##

n=0
while n<=5:
   print(n)
   n+=1

while True :
    a=int(input("first number: "))
    b=int(input("second number: "))
    print(a+b)
    repeat = input("end?: ")
    if repeat == "y":
        break

for i in range(1,5):
   for j in range(1,3):
      print(j, end="")
    print()

for i in range(1,5):
    for j in range(1,i+1):
        print(j, end=" ")
    print()


sum = 0
for i in range(1,51):
    if i%2 ==0:
     sum = sum + i
print("addition of even numbers: ",sum)


sum = 0
i = 0
while i <=100:
    i += 1
    if i%8==0 and i%12==0:
        sum += i
        print(sum)
print()

## billing in while true ##

while True:
    name = input("enter customer name: ")
    bill = 0
    while True:
        product = input("enter product name: ")
        bottle = 40
        fan = 100
        cup = 60
        if product == "bottle":
            price = 40
        elif product == "fan":
            price = 100
        elif product == "cup":
            price = 60
        else:
            print("invalid input")
            break
        quantity = int(input("enter the quantity: "))
        total = price*quantity
        bill += total
        repeat = input("more products? press y if yes and n for no : ")
        if repeat == "n":
            break
    print("Name: ", name)
    print("Your total bill is: rs", bill)
    print("Thank you for shopping have a great day")
    q = input("next customer? y or n: ")
    if q=="n":
        break


a = "hi how"
print(len(a))
print(a.count("f"))
print(a.upper())
print(a.casefold())  #..lower
print(a.capitalize())#...first letter caps
print(a.title())


a = "my name is : {}, my height is : {}"
h = "5'9"
name = "shreyes"
print(a.format(name,h))
print(name.center(15,'*'))
print(a.index("n",1,6))
print(name.center(10))

a= "shreyes ashok saalunke"
print(a[5:10])
print(a[5:])
print(a[-3:])
b = "123456789"
print(b[::2])
print(b[::-1])
print(b[6:1:-1])
print(b[2:5])

a =input("enter:")
b = sorted(a)
print(b)


## list ##

a = ["apple", "mango", 5,6]
print(a)
print(a[2])
print(a[-1])
print(a[1:3])
print(a[::-1])
a.append("hi")
print(a)
a.insert(2,"banana")
print(a)
a.remove("banana")
print(a)
a.pop(1)
print(a)

b = a.copy()
##or ##
b = [i for i in a]
print(b)

print(b)
c = [1,2,3]
b.extend(c)
print(b)
b.reverse()
print(b)
c.append(0)
print(c)
c.sort()
print(c)
c.clear()
print(c)

## dictionary ##
a = {"fruit" :"apple", "number" : 5}
for i in a:
    print(i)
for i in a:
    print(a[i])
for i in a.values():
    print(i)
for i,j in a.items():
    print(i,"-",j)
i = a.get("fruit")
print(i)
i = a.items()
print(i)
i = a.keys()
print(i)
i = a.copy()
print(i)
b = {"a":7,"g":5,"f":9}
c = sorted(b.values())
print(c)

a = {"hulk", "spidey", "thor", "captain"}
print(a)
a.add("ironman")
print(a)
a.pop()
print(a)
a.remove("thor")
print(a)
b = a.copy()
b.remove("hulk")
print(b)
print(b.issubset(a))
b.update(a)
print(b)
b.clear()
print(b)

## import datetime ##

x = datetime.datetime(2005,5,6)
print(x)
print(x.strftime("%a"))
print(x.strftime("%b"))
print(x.strftime("%m"))
print(x.strftime("%y"))
## import random ##
x = random.randint(1,100)
print(x)
l = ["heads", "tails"]
x = random.choice(l)
print(x)

## numpy ##

import numpy as np
a = np.array([5,6,3,1])
print(a)

