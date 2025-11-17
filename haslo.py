def waliduj_haslo(haslo):
    lowercases = 0
    uppercases = 0
    all_letters = 0
    numbers = 0

    for letter in haslo:
        if letter.isupper():
            uppercases += 1
        else:
            lowercases += 1
        if letter.isdigit():
            numbers += 1
        all_letters += 1
        
    if lowercases > 0 and uppercases > 0 and numbers > 0 and all_letters >= 8:
        return True
    else:
        return False


haslo = input("Podaj Hasło do sprawdzenia: ")

print(f"Warunki hasła spełnione? {waliduj_haslo(haslo)}")
