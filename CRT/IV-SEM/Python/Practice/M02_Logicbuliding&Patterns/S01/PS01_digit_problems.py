'''

1. write a python code to count digits of number?
ex: 15678 --> output :5

2.sum of the digits in a number?
ex: 12345 -->15
'''
'''
num= xint(input("Enter a number: "))
count = 0

if num == 0:
    count = 1
else:
    while num != 0:
        count += 1 
        num //= 10 


print(" number of digits", count)
'''
'''
num= int(input("Enter a number: "))
sum_digits = 0

num = abs(num)

while num > 0:
    digit = num % 10 
    sum_digits += digit
    num //= 10 

print("sum of digits: " , sum_digits)
'''
'''
num= int(input("Enter a number: "))
product = 1

num = abs(num)
if num == 0:
    product = 0
else:
    while num > 0:
        digit = num % 10 
        product *= digit
        num //= 10 

print("product of digits: " , product)

'''
'''
num = int(input("Enter number: "))
rev = 0 

while num > 0 :
    rev =  rev*10 + num%10
    num //= 10

print("Reverse: ", rev)
'''
'''
n = int(input("Enter n"))
even  = 0 
odd = 0 
while n > 0:
    d = n % 10 
    if d % 2 == 0 :
        even += 1
    else:
        odd += 1

    n //= 10 

print(even)
print(odd)
'''
'''
leetcode problem : reverse  number
given a signed 32 bit integer x, returns x with its digits reversed .if reversing x 
causes the value to go outside the signed 32 bit integer [-2^31,2^31,-1],then return 0.

'''
'''
n = int(input())
if n = 0:
    print(int(str(n)[::-1]))
else: 
    n = -1*n
    print(-1*int(str(n)[::-1]))
'''

'''
plus one
Problem Statement: Plus One

You are given a non-empty array of digits representing a non-negative integer.
The digits are stored such that the most significant digit appears first, and each element in the array contains a single digit.

Increment the integer by one and return the resulting array of digits.

The input number does not contain any leading zeros, except for the number 0 itself.

Example 1

Input: [1, 2, 3]
Output: [1, 2, 4]
'''
'''
class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits
'''
