# 12. Check if a String is a Palindrome

# Write a Python function that checks whether a passed string is a palindrome or not.

# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

word = input("podaj słowo do sprawdzenia: ")

if is_palindrome(word):
    print("slowo jest palindromem")
else:
    print("slowo nie jest palindromem")