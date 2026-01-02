#recursive
'''
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

x = int(input("Enter a number: "))
print("Factorial of x is:", fact(x))
'''
#non recursive
n = int(input("enter a number:"))
f = 1
for i in range(1, n+1):
    f *= i
print(f)
