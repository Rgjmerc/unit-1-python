"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""

def divide_numbers(num1, num2):
    result = num1 / num2
    print("Result:", result)

# Example usage:
try:
    divide_numbers(10, 0)
except:
    print("The second input is 0 so this cannot be divided.")

"""
Example 2: Opening Files
"""

def read_file(filename):
    file = open(filename, 'r')
    contents = file.read()
    print("File contents:", contents)
    file.close()

# Example usage:
try:
    read_file("nonexistent.txt")
except:
    print("This file does not exist so the action cannot be completed.")

"""
Example 3: List Items
"""

def get_item(lst, index):
    item = lst[index]
    print("Item:", item)

# Example usage:
my_list = [1, 2, 3]
try:
    get_item(my_list, 5)
except:
    print("There isn't an item in the list correlated to this number in the index.")

"""
Example 4: Dictionaries
"""

def get_value(dictionary, key):
    value = dictionary[key]
    print("Value:", value)

# Example usage:
my_dict = {"a": 1, "b": 2}
try:
    get_value(my_dict, "c")
except:
    print("There is no item in the dictionary corralated to this key.")


"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        print("Error: File not found.")
    else:
        print("File has been found")
    finally:
        print("Action Has Been Completed. If an error occured please retry.")

# Example usage:
process_file("example.txt")