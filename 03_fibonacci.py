
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter n: "))

if n < 0:
    print("Enter a non-negative number")
else:
    print("Fibonacci number:", fibonacci(n))