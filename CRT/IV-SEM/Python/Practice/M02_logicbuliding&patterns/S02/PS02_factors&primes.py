'''
read a number from a user and counter number  factor
'''
'''
n>=  = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

print("Number of factors:", count)

'''
'''
#check whether the given number is prime or not
'''
n = int(input())

for i in range(2, n):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")
