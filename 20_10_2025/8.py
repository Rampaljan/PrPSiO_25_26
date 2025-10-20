# 8. Return a New List with Distinct Elements from a List

# Write a Python function that takes a list and returns a new list with distinct elements from the first list.

# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def distinct(list):
    new_list = []
    for item in list:
        if item not in new_list:
            new_list.append(item)
    return new_list

list = [1,2,3,3,3,3,4,5]

print(f"Result: {distinct(list)}")