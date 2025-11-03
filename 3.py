# 3. Multiply All Numbers in a List

# Write a Python function to multiply all the numbers in a list.

# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

def multiplying(list):
    sum = 1
    for item in list:
        sum = item * sum
    return sum

list = [8, 2, 3, -1, 7]

print(f"Result: {multiplying(list)}")