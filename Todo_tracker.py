print("ToDo Tracker")
print("")
todo=[]
while 1:
    print("What would you like to do?")
    print("")
    print("1. View your ToDo's")
    print("2. Add a new ToDo")
    print("3. Edit a ToDo")
    print("4. Remove a Todo")
    print("5. Clear All")
    print("")
    print("Enter one of one of the numbers above.")
    choice = int(input(""))
    #input for original Choice
    print("")
    num = 1
    if choice == 1:
        for thing in todo:     
            print(f"{num}){thing}")
            num += 1
            #Prints all of the list one bt one with the order number ahead of it
        print("")
        print("---------------------------------------------------")
        print("")
    elif choice == 2:
        print("What Would you like to add?")
        add = input("")
        todo.append(add)
        #adds a item to the end of the list
        print("")
        print(f"Added {add} To Your ToDo List.")
        print("")
        print("---------------------------------------------------")
        print("")
    elif choice == 3:
        print("What would you like to edit?")
        edit = input("")
        print("")
        print("What would you like to change your ToDo To")
        change = input("") 
        todo[edit] = change
        #uses variables to change a prior item in the list to a new item in the list
        print(f"{edit} had been changed to {change}.")
        print("")
        print("")
        print("----------------------------------------------------")
        print("")
    elif choice == 4:
        print("What Would You Like To Remove?")
        remove = input("")
        todo.remove(remove)
        #removes a item in the list 
        print(f"Removed {remove} From Your ToDo List.")
        print("")
        print("---------------------------------------------------")
        print("")
    elif choice == 5:
        todo=[]
        print("Your ToDo list Is Cleared")
        #clears all data in the list
    else:
        print("That wasn't one of the options.")
        #in case something that wasnt an option was chosen