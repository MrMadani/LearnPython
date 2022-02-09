"""
name ="shahin"

age = 25
print("{} is {} years old".format(name,age) )#shortcut way of asigning any values in the print statemen

"""
"""
#operators
a=3+4
b=4-3
c=3*4
d=5/2
e=5//2      #// flow division. will give out the first int value of the result
f=2**2      #** will be used as exponent

print(" add = {}\n sub = {}\n mul={}\n div ={}\n flowDivision ={}\n exponent ={}\n".format(a,b,c,d,e,f))
name = input("enter the name =").strip()
print("my name is {}".format(name))
"""

"""
#using random module and changing a integer value to string 
import random
name=input("enter the name: ").strip()
userID=name + str(random.randrange(0,500,1))#assigning a random number with the name
print("the user ID is: {}".format(userID))
"""
"""
#for looping
num=[1,2,3,4,5,"good",30]
for number in num: #the for loop takes the num variable as list                                                                                 
        print(number)

"""

"""
#calculator using if condition
num1= int(input('enter the first number:').strip())
num2= int(input('enter the second number: ').strip())

opr=input('enter the operator:').strip()
add=sub=mul=div=0

if opr=='+':
    add=num1+num2
elif opr == '-':
    sub=num1-num2
elif opr == '*':
    mul=num1*num2
elif opr=='/':
    div=num1/num2
else:
    print("there is an error")
print("the result is {},{},{},{}".format(add,sub,mul,div))
"""
# 1
"""#adding user define functions key word is 'def'
def func_name(a,b="java"):
        return "i like {} and hate {}".format(a,b)

funcname=func_name("python")#using funcname for catching the value of the func_name 
print(funcname)
"""
"""
#calculator using fuctions
#calculator using if condition
#functions must defined before calling of assigning them
def add(a,b):
        return a + b
def sub(a,b):
        return a - b   
def div(a,b):
        return a/b
def mul(a,b):
        return a*b

num1= int(input('enter the first number:').strip()) #the declaration of the value is outside the
                                                    #function so it has the global scope,
                                                     #that is the variables can be used anywhere in the code 
num2= int(input('enter the second number: ').strip())

opr=input('enter the operator:').strip()


if opr=='+':
    print(add(num1,num2))
elif opr == '-':
    print(sub(num1,num2))
elif opr == '*':
   print(mul(num1,num2))
elif opr=='/':
    print(div(num1,num2))
else:
    print("there is an error")
"""
"""
#packing and unpacking
def add(*args): #the *args will be used as a tuple
        total = 0
        for i in args:
                total = total + i
        return total

print(add(1,2,3,4,5,6,7))

"""
"""
#write statement
inp = input("enter what you like about python ").strip()

with open("with.txt","a") as f: #the second parameter in perenthesis is mode perform
                                #open for reading (default)open for writing, truncating the file first
                                # 'x'	create a new file and open it for writing
                                # 'a'	open for writing, appending to the end of the file if it exists
                                # 'b'	binary mode
                                # 't'	text mode (default)
                                # '+'	open a disk file for updating (reading and writing)
                                # 'U'	universal newline mode (deprecated) 
         f.write(inp)

with open("with.txt","r") as f:
        print(f.read())
"""

"""
question = input("Do you want to play: ")
answer = question.lower()
if answer != "yes":
        exit()

answer= input("what is the capital city of bangldesh: ").lower()
score = 0
if answer == "dhaka" :
        print("correct!")
        score +=1
else: print("incorrect")
answer= input("enter the city where port is located: ").lower()
if answer == "chittagong":
        print("correct!")
        score +=1
else:
        print("incorrect")

print("your score is "+str(score)+"")
"""
# list data types
"""
listName = [1,2,3,4,1,5,bool,"hello"]       #can hold muliple types of data
print(listName)
listName = [[1,3,3],'hello',[2,3,4],6,5,445,23,55,20]       #nested list can also be created in the list variable
print(listName[4:7:2])      #will show the values from the 4th index before the 7th index and the step will be 2 index at atime
print(*listName)
listName.append([2,32,33,41]) #will insert multiple element in the list 
listName.insert(2,[2,32,33,41]) #will add the following elements in the list
listName.remove('hello')#do not need to use the index to delete any value
listName.pop(1)
print(listName)
"""
"""
number= input("enter a number: ")
if number.isdigit():             #will check if the given value is a digit or not and returns boolean values
                                #if we use 'is' before any methods we can check if it is that type or not
        print("the number is a digit")
else: 
        print("not a number! ")
"""
# String

myString = '''hello '''
print(len(myString))  # will give the length of the string variable
myString2 = "Shahin Madani"
print(myString2[1:8])  # will give the value form the 1 index to 8th index
myString = (myString + myString2).upper()
print(myString)

'''
# dictionary 
#it is a unorderd collection of data 
# it has the key : value pair
my_dict = {}

my_dict1 = dict([(1,'apple'),(2,'banana')])
my_dict = {"name" : "python", "work" : "programer"}

for key,value in my_dict.items():
        print("{} is {} ".format(key,value))

my_dict.get(1) #searches with the key

my_dict[1] = 'bangladesh'#will update the value of the key 1

'''
"""
#tuples
#we cannot change of the element of the tuple 
#but we can change the value of the list not the tuple
#can have mixed data types as well as nested tuple
my_tuple = ("cat",[6,6,34,44],True)
           #   0,       1,      2


my_tuple[1]
my_tuple[2][2]

"""
"""
#object oriented python
class Bird:
        def __init__(self, name, age): #tthe first method of a class is the constructor
                                       # 
                self.name= name 
                self.age=age
        def sing(self , song):
                return "{} sing {}".format( name,song)
penguin = Bird()"""


































