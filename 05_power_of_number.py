
def power(x, n):
    if n == 0:
        return 1

    return x * power(x, n - 1)

x = float(input("Enter the base: "))
n = int(input("Enter a non-negative exponent: "))

if n < 0:
    print("Exponent must be non-negative")
else:
    print("Result:", power(x, n))