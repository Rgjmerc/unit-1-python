print("Welcome to Calc-Inator 5000")
print("")
print("")
x = float(input("Enter First Number: "))
print("")
y = float(input("Enter Second Number: "))
#entering numbers
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
#all choices
choice = int(input("Enter Choice: "))
#choice
if choice == 1:
    addition = x+y
    print (addition)
    #addition
elif choice == 2:
    subtraction = x-y
    print (subtraction)
    #subtraction
elif choice == 3:
    multiplication = x*y
    print (multiplication)
    #multiplication
elif choice == 4:
    division = x/y
    print (division)
    #division
elif choice == 5:
    floor = x//y
    print (floor)
    #floor
elif choice == 6:
    expo = x**y
    print (expo)
    #exponent
elif choice == 7:
    remainder = x%y
    print (remainder)
    #remainder