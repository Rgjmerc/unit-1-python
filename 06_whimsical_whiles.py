"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""

x=1
while x<=10:
    print (x)
    x+=1
    #forward
print("")

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""

y=10
while y>=1:
    print (y)
    y=y-1
    #reverse
print("")

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""

factorial= int(input("Enter a number "))
number=factorial-1
while number>1:
    factorial=factorial * number
    number = number - 1
    #math for factorial
print (factorial)

"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""

pswd_attempt=input("Enter a password attempt: ").lower
password = "password"
while pswd_attempt != password:
    print ("Incorrect Password")
    pswd_attempt=input("Enter a password attempt: ")
    #loops attempts until correct
else:
    print("Correct Password")

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""


"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""

