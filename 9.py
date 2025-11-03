# 9. Check Whether a Number is Prime

# Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

def is_prime(n):
    dzielniki = 0
    for i in range (1, n+1):
        if n%i == 0:
            dzielniki += 1
    if dzielniki == 2:
        return True
    else:
        return False

n = int(input("Podaj liczbę do sprawdzenia: "))

if is_prime(n):
    print("Liczba jest pierwsza")
else:
    print("liczba nie jest pierwsza")