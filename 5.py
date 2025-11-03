# 5. Factorial of a Number

# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return(result)

n = int(input("Podaj liczbe do wyznaczenia factorial z niej: "))

print(factorial(n))