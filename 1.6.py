def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

print("Result:", power(base, exp))
