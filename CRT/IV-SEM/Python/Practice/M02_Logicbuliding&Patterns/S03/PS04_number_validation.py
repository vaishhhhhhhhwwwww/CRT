'''
Armstrong number problem

n = int(input())
l = len(str(n))
res = 0
for i in str(n):
    res += int(i) ** l

print("Armstrong" if n == res else "not Armstrong")

'''
