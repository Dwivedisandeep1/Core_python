# Recursion
# Calling function on its own fuction

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)


num = 25
print(f"Number {num}")
print(f"Factorial {factorial(num)}")
print(5 * factorial(4))

f0 = 0
f1 = 1
f2 = f1 + F0


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(19))
