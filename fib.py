num = input("Enter a number: ")

def fib(n):
    n = int(n)
    if n == 1 or n==2:
        return 1
    else:
        return (fib(n-2) + fib(n-1))

print(fib(num))