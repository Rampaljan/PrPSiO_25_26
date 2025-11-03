# 7. Count Uppercase and Lowercase Letters in a String

# Write a Python function that accepts a string and counts the number of upper and lower case letters.

# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

str = 'The quick Brow Fox'

def licz(str):
    lower = 0
    upper = 0 

    for char in str:
        if 65 <= ord(char) <= 90:
            upper += 1
        elif 97 <= ord(char) <= 122:
            lower += 1
    print(f"male litery: {lower}")
    print(f"wielkie litery: {upper}")

licz(str)

    