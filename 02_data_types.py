"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
Password = "hello"
Entr_Pswd = input("Enter Password ").lower()
if Entr_Pswd == Password:
    print ("Correct")
else:
    print("Incorrect")

"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
smth=input("Type something ")
smths=smth.strip()
if bool(smths) == True:
    print("Valid")
else:
    print("Invalid")

"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
cat = "Cat".lower()
dog = cat.replace("cat","Dog").lower()
print(cat)
print(dog)
"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
age=int(input("Enter age "))
txt = f"You are {age} years old."
print (txt)

"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""

decimal1 = float(input("Give me a decimal number "))
decimal2 = float(input("Give me another smaller decimal number "))
answer = decimal1 / decimal2
quotent = f"{decimal1} / {decimal2} = {answer:.1f}"
print(quotent)