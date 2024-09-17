"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
decimal = 12.9
print (int(decimal))
# Converting float to integer & printing
print (decimal)
# Printing original float

"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
Random_Number=int(input("Choose a number "))
#entering number
if Random_Number > 0:
    print("This number is Positive")
    #checking if positive
elif Random_Number < 0:
    print("This number is Negative")
    #checking if negative
else:
    print("This is Zero")
    #just in case of 0

"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
Enter_Float = float(input("Enter a decimal number "))
Enter_Numeral = int(input("Enter a whole number "))
# Variables inputs
Sum = Enter_Float + Enter_Numeral
Product = Enter_Float * Enter_Numeral
Difference = Enter_Float - Enter_Numeral
Quotent = Enter_Float / Enter_Numeral
#The math
print (Enter_Float)
print ("+")
print (Enter_Numeral)
print ("=")
print (Sum)
print ("")
print ("")
print (Enter_Float)
print ("x")
print (Enter_Numeral)
print ("=")
print (Product)
print ("")
print ("")
print (Enter_Float)
print ("-")
print (Enter_Numeral)
print ("=")
print (Difference)
print ("")
print ("")
print (Enter_Float)
print ("/")
print (Enter_Numeral)
print ("=")
print (Quotent)
print ("")
print ("")
#Printing all the math

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
Fruit_Inventory = {
    'Mangos': 3,
    'banana':5
#the fruit keys
}
print (Fruit_Inventory["Mangos"])
#printing from the dictionary

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""

General_String = "1,5,3,2,4"
My_Tuple = General_String.split(",")
#conversion of sting into tuple
print (General_String)
print (My_Tuple)
#Printing both string and tuple