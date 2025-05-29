MENU = "(G)et a valid score \n(P)rint result\n(S)how stars \n (Q)uit"
def main ():
    print(MENU)
    choice = input ("Enter your choice:").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Enter your score:"))
            score = get_valid_score (score)
        elif choice == "P":
            #score = float(input("Enter your score:"))
            print (get_result (score))
        elif choice == "S":
            score = float(input("Enter your score:"))
            print (show_star (score))
        else:
            print ("Invalid option, please try again.")

        choice = input("Enter your choice:").upper()
        print ("Farewell")

def get_valid_score (score):
    while score < 0 or score > 100:
        return "Invalid score"
    return score

def get_result (score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"

def show_star (score):
    return '*' * int(score)

main()


