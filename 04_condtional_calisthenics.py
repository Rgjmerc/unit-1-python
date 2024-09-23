'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''

ger = 12
if ger > 10 and ger % 2 == 0:
    #checking for remainder after dividing by 2
    print("True")
else:
    print("False")

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''

student = False
age = 18
if age <= 18 or student == True:
    #setting condition to either or
    print ("The price is 10$")
else:
    print("The price is 20$")

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''

fruit = input("Enter the name of a fruit.  ").lower()
fruit_list = ["mango", "cucumber", "avocado","banana","pineapple"]
if fruit in fruit_list:
    print("Yes, that fruit is in the list.")
    #find in the list
else:
    print("No, that fruit is not in the list.")

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''

year = int(input("What year is it? "))
if year % 400 == 0:
    print("It is a century and leap year.")
    #divide by 400 and no remainder
else:
    print("Not a century and leap year.")

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

kilo = int(input("How many kilograms is the order weight "))
if kilo > 0:
    print("Error Invalid Input.")
    #if less than 0
Zone_A = 5
Zone_B = 7
print (f"Shipping cost for Zone A is ${kilo*Zone_A} and shipping cost for Zone B is ${kilo*Zone_B}")
#the math

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''

Side_A = int(input("Side Length A "))
Side_B = int(input("Side Length B "))
Side_C = int(input("Side Length C "))
# INPUTS FOR TRIANGLE SIDES
if Side_A == Side_B and Side_B == Side_C:
    print("This is an Equalateral Triangle")
elif (Side_A == Side_B and Side_B != Side_C) or (Side_A != Side_B and Side_B == Side_C) or (Side_A == Side_C and Side_B != Side_C):
    #all variants of isoceles
    print ("This is an Isocsceles Triangle")
elif ((Side_A != Side_B and Side_B != Side_C) and (Side_A + Side_B > Side_C) or (Side_A + Side_C > Side_B) or (Side_B + Side_C > Side_A)):
    print ("This is a Scaline Triangle")
else:
    print("Not a Triangle")