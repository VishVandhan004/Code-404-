import sqlite3
from math import pi
import math
#    PYTHON
# anything is absolutely fine, you could use either single qoutes or double quotes
print("python is fun")
a, b = 20, 2
print(a+b, a-b, a*b, a % b, a/b)
print(a//b)  # floor division - you'll get an integer result not a fucking decimal
print(a**b)  # exponent
# formatting the numbers
print("The sum of {0} and {1} is {2}".format(a, b, a+b))
# in Variables, it's better to start with a lowercase variable name and it can have underscores too. It shall not start with capital name or numbers
# Changing the values of the variables
country = "UAE"
print(country)
country = "USA"
print(country)
# assigning the variables in a single statement
x, y, z = 1, 2, 3
print(x, y, z)

# printing something at the start and the end
print('Stop it, get some help', end='!!!')

# MULTI-LINE STATEMENT -> we can also write our statements like this by adding an '\' to the statement
b = 1 + 2 + 3 + \
    4 + 5 + 6
print(b)

# "PASS" statement is a placeholder for the future. it doesn't produce any output on the screen and it hasn't got any value to it.

# Constants - constants are the normal stuff like the one you know. example - shit like PI=3.14, GRAVITY = 9.8,etc .. Constants must always be in UPPERCASE letters
# Literals - Literals are the data given in the variables. They are immutable(can't be changed)
# example of numeric literals -
num1 = 0b0101  # binary number
num2 = 0o310  # octal number
num3 = 0x12c  # hexadecimal number
print(num1, num2, num3)
# string literals contain unicode characters
# whenever we use the type function in our code, wee need to get the class in the output
v = 10
print(type(v))
# NOTE  -> Rememeber that, in slicing the first value will be inclusive and the second value will be exclusive

# literal collections - list, tuple, set, dictionary

# LISTS
# Lists are like arrays in C. ordered sequence. store many types of data. Objects are in square bracket.
numbers = [1, 2, 3, 4, 'hi']  # List # type: ignore
print(numbers[0], numbers[4])
print(numbers[1:])
print(numbers[0:3])
print(numbers[::-1])
numbers[0] = 0  # changing a particular value in lists
print(numbers)
# TUPLES
# Its an ordered sequence, immutable
# slicing is possible but only changing values are not possible
alphabets = ("a", "b", "c", 30)
print(alphabets[0], alphabets[3])
print(alphabets[::-1])
print(alphabets*3)
# STRINGS
# strings are the sets of characters , they are immutable
str1 = "Hello"
print(str1[0])
# SETS
# Sets are collection of unordered items. kinda bullshit. does not support indexing.
set = {1, 3, 5, 7}
print(set)
# DICTIONARIES
# Its a kind of an unordered collection, data is in the form of key:value pair. it has curly braces
dict = {1: "China", 2: "Taiwan"}
print(dict)
print(dict[1])  # accessing values using keys
n = 5
print(str(n))
print(type(n))
# Output built-in function
# the below method is a method in the print() function
print(1, 2, 3, 4, sep="*")
# Input
print("Hi {name}, {greet}".format(greet="welcome", name="Joe"))
# Import
'''
there are basically 2 ways to import a stuff from python
1. Importing the whole thing
2. importing only some stuff from a whole bunch
'''
# below is the 1st case
print(math.pi)
# below is the 2nd case
print(pi)
# there are some ways to import like          "from math import *"
# IF-ELSE Statement
age = int(input("Enter age"))
if age >= 18:
    print("You can vote")
else:
    print("Get the hell outta here man")

# IF,ELSE,ELIF Conditional Statements
# exp-1
marks = int(input("Enter your marks: "))
if marks >= 80:
    print("you got A grade")
elif marks >= 70:
    print("You got B grade")
else:
    print("supply rasko po")
# exp-2
age = int(input("Enter your age : "))
if age < 5:
    print("go sleep")
elif age == 5:
    print("Go to LKG")
elif ((age > 5) and (age <= 17)):
    print("Go to school")
else:
    print("Go to College")
# exp-3
n = int(input("enter a number"))
if n >= 0:
    if n == 0:
        print("ZERO")
    else:
        print("Positive Number")
else:
    print("Negative Number")

# TYPE CONVERSIONS
num_int = 123
num_str = "456"
print(type(num_int))
print(type(num_str))
# one is an integer and one is a string, if you want to add, you need to convert the string into an integer and then do the respective operation
num_str = int(num_str)
print(num_str + num_int)

# WHILE LOOP - first comes the initialization, then comes the condition and then comes the increment or decrement
i = 1
while i < 3:
    print(i)
    i += 1
# break situation
k = 1
while k < 6:
    print(k)
    k += 1
    if k == 4:
        break
# break -> break statements are used to stop and exit from the loop
# FOR-LOOP
fruits = ["apple", "orange", "kiwi"]
for x in fruits:
    print(x)
for i in range(1, 8):
    if i == 5:
        continue
    print(i)
for i in "Python":
    print(i)
# the below for loop is used to do a particular thing a set of times
for j in range(2):
    print("I'm High")
for x in range(2, 7):
    print(x)
# Here in range(2,7) -> 2 is inclusive and 7 is exclusive. 2 is included and 7 isn't included.
# in the below for-loop, we start the iteration from 0, it goes on till 30, and it increments by 3..
# the second value(30) is not considered
for x in range(0, 30, 3):
    print(x)
# LISTS AND SOME STUFF RELATED TO IT
fruits = ["apple", "orange", "kiwi", "litchi"]
# need to put characters/strings in double quotes. not required for numbers,boolean
mixed_list = [2.5, 44, "a", "b"]
print(fruits)
print(fruits[0])  # indexation
print(fruits[::-1])  # reversing the whole thing
print(fruits[1:])  # printing from a particular thing
# Another way of iterating through a list is by using an iterator. we initiliaze it by using the "iter" to the list. after that , we can continue by using the "next" method
# fruits = iter(fruits) #starts the iterator
# print(next(fruits))  # prints the elements
# print(next(fruits))
# print(next(fruits))
if "apple" in fruits:
    print("YAY")
# insert method is used to insert a value at a particular index
fruits.insert(1, "mango")
# append is used to insert an element at the last of the list..
fruits.append("banana")
fruits2 = ["melon"]
# this method is used to extend the list by adding another list to it
fruits.extend(fruits2)
# fruits = fruits + fruits2 -> [concatenation of 2 lists]
fruits.remove("melon")  # removing a particular value
fruits.pop(3)  # removes a value at an index
# del fruits[3]  ->it is also another type of method to delete the element from the list at a particular index.
print(fruits)
print(len(fruits))
print(mixed_list)
print(type(mixed_list))

# MULTI-DIMENSIONAL ARRAY
multd = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(multd)
print(multd[0])
print(multd[3])
print(multd[2][1])

# TUPLES AND SOME STUFF RELATED TO IT..
fruits = ("apple", "banana", "cherry")
print(len(fruits))
mix_t = ("hi", 1, 2.3)
print(mix_t)
print(mix_t[0])
print(mix_t[::-1])
print(mix_t[0:2])
# most of the operations of tuples are same as that of lists, but the only difference here is we cannot change the values of the tuple.
# if you want to change a value in the tuple, you need to convert the tuple into a list, after converting into list, change the required value and convert it back into the tuple
fruits_l = list(fruits)
fruits_l[1] = "melon"
fruits = tuple(fruits_l)
print(fruits)
# tuple packing -> tuple can also be created without using paranthesis. it's tuple packing. we can also access elements from it. it's called tuple unpacking
tuple4 = 101, 102, 103, "Airbnb"
print(tuple4[0])
tuple5 = 'w', 'e', 'l', 'l'
print(tuple5.count('l'))  # counting a shit for no.of.times
print(tuple5.index('e'))  # gives the index of a value
tuple6 = 22, 44, 11, 4, 5, 6
print(len(tuple6))
print(min(tuple6))
print(max(tuple6))
print(sorted(tuple6))
# NESTED TUPLE
nest_tuple = ('point', (1, 2, 3))
print(nest_tuple)
print(nest_tuple[0][1])  # accessing elements
print(nest_tuple[1][2])
# we can't seperately delete the values from the tuple. if we really want to do that, we can delete the whole shit by using "del tuple4"

# SETS AND SOME OTHER STUFF
# sets might be printed in an unordered manner. they are unordered. you might get a different order every single time when you print the output
fset = {"apple", "lemon", "kiwi"}
print(fset)
print(len(fset))
mset = {True, "Hi", 1, 2.4}
print(mset)
for x in mset:
    print(x)
fset.add("orange")  # "add" method in sets
fset.update(["lemon", "cherry"])  # "update" method in sets
fset.remove("cherry")  # "remove" method in sets
fset.discard("orange")  # "discard" method in sets
fset.pop()  # pop() -> removes the last element( remember, sets are unordered, so you don't know what's the last element)
print(fset)
# DICTIONARY AND SOME STUFF OF THAT SHIT
dict = {1: "One", 2: "Two", 3: "Three"}
dict[4] = "Four"  # adding another element
print(dict[1])  # PRINTing the first element
x = dict.keys()  # getting the keys of a dictionary
print(x)
x = dict.values()  # getting the values in dictionary
print(x)
x = dict.items()  # items -> has both keys and values
print(x)
dict[1] = 10  # changing the values
dict.update({2: "20"})  # updating the values
dict.pop(4)  # deleting a particular index
print(dict)  # printing the whole thing
# FUNCTIONS  ->block of code which can be used again and again


def function():  # syntax for creating a function
    print("hello")


function()      # calling a function

# FUNCTION USING PARAMETRES


def hi_func(name):
    print("hi " + name)


hi_func("Joe")

# LIST AS AN ARGUMENT


def fruits(name):
    for i in name:
        print(i)


fruit_name = ["Apple", "kiwi", "litchi"]  # this is the list
fruits(fruit_name)  # passing list as an argument

# Using "return" statement


def degrees(x):
    return 15*x  # return -> returns a value and exits from the function.


print(degrees(2))


def new_names(n1, n2, n3):
    print("The first name is " + n1)
    print("The second name is " + n2)
    print("The third name is " + n3)


new_names("Joe", "Vlad", "Trump")

# Arbitrary arguments  -> when you don't know how many arguments you're going to pass, you need to place an asterisk beside an argument


def fruits_1(*name):
    print("The fruit is " + name[0])
    print("The fruit is " + name[1])
    print("The fruit is " + name[2])


fruits_1("Apple", "Kiwi", "litchi")

# RECURSIVE FUNCTION  -> A function calling itself to solve the problem. we use only functions in recursion. we don't use loops or any other kind of iteration
# here, we take numbers and print the sum using recursion


def numbers(n):
    if (n > 0):
        result = n + numbers(n-1)
        print(result)
    else:
        result = 0
    return result


numbers(6)
# here you'll get 6 values starting from numbers(0), numbers(1), ....to numbers(6) the way to solve this is: numbers(0) = 0 ,                   numbers(1) = 1+numbers(0) = 1+0 = 1, and so on........

# Classes and Objects
# OOPS -> Object Oriented Programming is a method of structuring the program by bundling props to objects.
# Class -> class is an object constructor. we use class to create the object
# 1st EXP


class NewClass:   # creating a class
    num = 10


print(NewClass)
p1 = NewClass()  # assigning it to a variable
print(p1.num)
# 2nd EXP


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hi(self):
        print('hi ' + self.name)


ob1 = Person("Dony", 40)
print(ob1.name)
print(ob1.age)
ob1.hi()
ob1.age = 50  # modification of objects
# 3rd EXP


class MycomplexNo:
    def __init__(self, real=0, imag=0):
        print("constructor is executing")
        self.real_part = real
        self.imaginary_part = imag

    def display_complex(self):
        print("{} + {}j is the complex Number".format(self.real_part, self.imaginary_part))


cmplx1 = MycomplexNo(40, 50)
cmplx1.display_complex()
del cmplx1.real_part  # deleting a particular thing
# print(cmplx1)
# del ob1   -> this is used to delete any object
# here __init__ function is used when the class is initiated. we can use it to assign value to object props. Here self is a reference to the object props

# FILE HANDLING
# modes of file are -> r(read a file),a (append in a file),w(writing in a file), x(creates a specified file)
f = open("demo.txt", "r")
# print(f.read()) -> reads and prints everything
# print(f.read(7)) ->only upto a cetain lines
for x in f:  # used to print the values using loop
    print(x)
# we just created a new file and wrote in that new file
f = open("main.txt", "a")
f.write("Another file is created and we wrote to it..")
f.close()
f = open("main.txt", "r")
print(f.read())

# NUMPY -> Numerical Python. It's a python library. used for linear algebra, matrices, etc..

# MATPLOTLIB -> it's a python package used to build the plots. used for scientific publications. also used in microsoft excel

# CONNECTING DB TO PYTHON
# WE WILL BE USING sqlite3
# sqlite3  -> it's a light-weight database which doesn't require a separate server
# OPENING A DATABASE
con = sqlite3.connect("OurDB.db")
print("You can see Database opened")
# CREATING A TABLE IN DATABASE
cur = con.cursor()
cur.execute('CREATE TABLE PRODUCT')
