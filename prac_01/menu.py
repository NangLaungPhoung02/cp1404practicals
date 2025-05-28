MENU = "(H)ello \n(G)oodbye\n(Q)uit"
print (MENU)
name = input ("What is your name?:")
choice = input ("Enter your choice:").upper()
while choice != "Q":
    if choice == "H":
        print(f" Hello {name}.")
    elif choice == "G":
        print (f"Goodbye {name}.")
    else:
        print ("Invalid choice.")
    print(MENU)
    choice = input("Enter your choice:").upper()
print ("farewell")