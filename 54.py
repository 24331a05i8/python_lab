#recursive
'''
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

x = int(input("Enter a number: "))
for i in range(x):
    print(fib(i), end=" ")
'''
#non recursive
n = int(input("enter a number:"))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a+b
