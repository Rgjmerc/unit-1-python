"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""

example = ["one","two","three","four"]
print(example)

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""

example.append("five")
#adding to the list
print(example)

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
example.remove("one")
#removing from list
print(example)

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""

example[0] = "one"
#changing items in the list
print(example)

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""

example.append("six")
example.append("seven")
#adding 2 things to the end of list
print(example)

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""

del example[0]
#deleting first thing in the list
print(example)

"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""

new = example[0:2]
#adding first 2 items in origional list to a new variable
print (new)

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
num = ["eight","nine","ten"]
final = example + num
#creating a new list to combine with origional list
print(final)