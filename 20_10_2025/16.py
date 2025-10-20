# 16. Create and Print a List of Squares for Numbers 1 to 30

# Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).

def squared():
    list = []

    for i in range (1, 31):
        list.append(i*i)

    return list

print(f"Result: {squared()}")