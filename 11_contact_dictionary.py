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
    print("")
    if choice == 1:
        print(dict)
        print("")

    elif choice == 2:
        add_name=input("What's the name of the person whose number you would like to add? ")
        print("")
        add_num =input(f"Add {add_name}'s number. ")
        print("")
        contact_book[add_name]=add_num
    elif choice == 3:
        del_name = input("W")

