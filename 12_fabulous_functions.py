import math
"""
Task 1: Greeting
Write a function that takes a name as a 
parameter and prints a greeting message like "Hello, [name]!".
"""

def greeter(name, greeting="Hello"): 
    print( greeting + " " + name )
greeter("Chimmychangas", "Greetings")

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

def square(num):
    return num * num
print(square(5))

"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""

def even_odd(digit):
    if digit % 2:
        return True
    else:
        return False
print(even_odd(25))

"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""

def area(length, width):
    return length * width
print (area(5,7))

"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

def degree_tran(celcius):
    fahrenheit = (celcius * (9/5)) + 32
    return fahrenheit
print(degree_tran(8))

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""



"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, and returns the total.
Your function should also optionally accept a 3rd argument for discount, and return the discounted if provided.
"""