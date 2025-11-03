# 6. Check if a Number Falls Within a Given Range

# Write a Python function to check whether a number falls within a given range.

def check(n, max, min):
    if n <= max and n >= min:
        return True
    else:
        return False
    
n = int(input("podaj liczbę do sprawdzenia: "))
min = int(input("podaj minimalny zakres: "))
max = int(input("podaj maksymalny zakres: "))

if check(n, max, min):
    print("liczba mieści się w zakresie")
else:
    print("liczba nie mieści się w zakresie")