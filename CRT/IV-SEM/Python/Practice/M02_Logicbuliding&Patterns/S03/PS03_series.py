'''
Arthematic series

a = int(input())
d = int(input())

for i in range(10):
    print(a+(i*d),end=" ")

Fibbonacci series
n = 10
a, b = 0, 1

print("Fibonacci Series:", end=" ")

for i in range(n):
    print(a, end=" ")
    
    a, b = b, a + b

using list;
1 method
    fib = [0, 1]
for i in range(8):
    
    next_value = fib[-1] + fib[-2]
    fib.append(next_value)

print(fib)
2 method
n = int(input())
li  = [0,1]
for i in range(2,n):
    li.append(li[i-2]+li[i-1])

print(li)


'''
n = int(input())
for i in range(1,11):
    print(n ** i,end = " ")