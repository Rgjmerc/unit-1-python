contact_book = dict()
while True:
    print("What would you like to do?")
    print("")
    print("1. View your Contact List")
    print("2. Add a new Contact")
    print("3. Remove a Contact")
    print("4. Exit")
    print("")
    print("Enter one of one of the numbers above.")
    choice = int(input(""))
    #allows for the choice to be made
    print("")
    if choice == 1:
        print(contact_book)
        print("")
    elif choice == 2:
        add_name=input("What's the name of the person whose number you would like to add? ")
        #takes the input for the dictionary key
        print("")
        add_num =input(f"Add {add_name}'s number. ")
        #takes the value for the dictionary
        print("")
        contact_book[add_name]=add_num
        #adds a new item to the dictionary combining the key and value taken previously
        print("")
        print("--------------------------------------------------")
        print("")
    elif choice == 3:
        del_name = input("What contact would you like to delete? ")
        #takes the value for the key to be deleted
        print("")
        del contact_book[del_name]
        #deletes the item by using the given key
        print(f"Deleted {del_name}'s contact")
        print("")
        print("--------------------------------------------------")
        print("")
    elif choice == 4:
        print("Exiting")
        #exits from the code 
        break