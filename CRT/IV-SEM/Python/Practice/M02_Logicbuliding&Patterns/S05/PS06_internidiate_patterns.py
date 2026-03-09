'''
Docstring for iv th sem.python.Assignments.M02_logicbuliding&patterns.S05.PS06_internidiate_patterns

squares of given list
li = [1,2,3,4,5]
res = []
for i in li:
    res.append(i ** 2)
print(res)

only even

li = [1,2,3,4,5]
ans = [i**2 for i in li if i % 2 == 0]


print(ans)

join mulyiple strings 
li = ['a', 'b' , 'c']
#' a b c '
ans = ' '.join(li)
print(ans)

n = 4

INTERMIDIANTE patterns 
n = 4 
1.output:
      *
     * *
    * * *
   * * * *
n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

2. inverted pyramaid
output:
* * * * 
 * * * 
  * *
   * 

n = int(input())
for i in range(n , 0 ,-1):
    print(" " * (n - i) + "* " * i)

3.diamond
n = 4

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)

output:
   * 
  * * 
 * * * 
* * * * 
 * * * 
  * * 
   * 

4.number pyramid

n = 4
output:
     1
    1 2
   1 2 3
  1 2 3 4
n = int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=mm8" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()
n = int(input())
for i in range(1,n+1):
        print(" "*(n-1)+" ".join([str(k) for k in range(1,i+1)]))
'''

