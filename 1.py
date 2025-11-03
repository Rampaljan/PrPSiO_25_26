# 1. Maximum of Three Numbers

# Write a Python function to find the maximum of three numbers.

list = [1,2,3]

def maximum(list):
    biggest = 0
    for item in list:
        if item > biggest:
            biggest = item
    return biggest

print(f"najwieksza liczba z podanych trzech to: {maximum(list)}")