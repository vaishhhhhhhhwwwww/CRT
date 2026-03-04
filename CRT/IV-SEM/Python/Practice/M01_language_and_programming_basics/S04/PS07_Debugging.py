'''
Debuging in python:
bug --> Error
Debugging --> Finding and fixing error

Types for error:
1.syntax error --> missing of colun,missing of identation
2.runtime error --> division by zero
3.logical error --> missing of logics

Debugging techniques:
1.print()
2.try-except
3.using pdb
    pdb --> python debugger
    purpose:
    1.pause the execution
    2.inspect the variable's value
    3.to run the code line by line
pdb commands:
1.n --> to execute the output in a next line 
2.p variable --> to get the value of a variable
3.l --> list nearby code
4.c --> continue the execution
5.s --> to start a function
6.r --> return from the function
7.h --> help
8.q  --> quit the execution
'''
try:
    a = int(input("Enter a number: "))
    print(10/a)

except ZeroDivisionError:
    print("can not be divisible by zero.")

except ValueError:
    print("invalid input")

'''
import pdb

def add(a,b):
    pdb.set_trace()
    return a+b 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(add(a,b))
'''