def prime(n, i=2):
    if n <= 1:
        return False
    if i == n:
        return True
    if n % i == 0:
        return False
    return prime(n, i + 1)

x = int(input("Enter a number: "))
print("Prime" if prime(x) else "Not Prime")
