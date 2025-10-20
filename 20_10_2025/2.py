# 2. Sum All Numbers in a List

# Write a Python function to sum all the numbers in a list.

# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def addition(list):
    sum = 0
    for item in list:
        sum = item + sum
    return sum

list = [8, 2, 3, 0, 7]

print(f"Result: {addition(list)}")
