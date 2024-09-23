print("Welcome to Calc-Inator 5000")
print("")
print("")
x = float(input("Enter First Number: "))
print("")
y = float(input("Enter Second Number: "))
print("")
print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor division")
print("6. Exponential")
print("7. Remainder")
print("")
choice = int(input("Enter Choice: "))
if choice == 1:
    addition = x+y
    print (addition)
elif choice == 2:
    subtraction = x-y
    print (subtraction)
elif choice == 3:
    multiplication = x*y
    print (multiplication)
elif choice == 4:
    division = x/y
    print (division)
elif choice == 5:
    floor = x//y
    print (floor)
elif choice == 6:
    expo = x**y
    print (expo)
elif choice == 7:
    remainder = x%y
    print (remainder)