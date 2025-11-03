# 4. Reverse a String

# Write a Python program to reverse a string.

# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def reverse(word):
    return word[::-1]

word = input("podaj słowo do odwrócenia: ")

print(f"Reversed: {reverse(word)}")