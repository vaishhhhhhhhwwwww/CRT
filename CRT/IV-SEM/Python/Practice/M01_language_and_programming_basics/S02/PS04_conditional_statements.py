
#read the number from the user ,check whether it is +ve ,-ve or zero

'''
input : 10
output:+ve
input: -4
output : -ve
input : 0
output:'zero'
'''
n = int(input())
if n > 0:
    print("positive")

elif n < 0 :
    print("negative")

else:
    print("zero")


