text = "Hello, world, my name is"
count = 0

for char in text:
    if char == " ":
       #there was no space in the string
        count += 1

print(count)



print("give me a number")
n = int(input())
#was registering as a string input so int() was added ahead of the input

for num in range(1, n):
    if num % 2 == 0:
        #sign needed to be changed from a < to a ==
        print(num, "is even.")
    else:
        print(num, "is odd.")



num = int(input("Enter an integer: "))

if num < 0:
  #changed from -1 to 0 so that no negatives would be added
  print("No negative numbers.")
else:
  result = 1
  for i in range(1, num):
    result *= i   

  print(f"Factorial of {num} is {result}")
  #made into an f string so that there wouldnt be an issues with string ans int combination


attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password: ")
    attempts += 1

    if password == correct_password:
        #changed from == "incorrect_password" to == correct_password
        print("Correct password!")
        break
    #added a break so that code would stop after correct password was reached
    else:
        print("Incorrect password")

    if attempts >= 3:
        #changed from > to >= 3 attempts to make it so it would actuall stop after 3 attempts and not 4
        print("Too many attempts")
        break