""" word occurrences
Estimate : 40 minutes
Actual: 1 hour and 15 minutes """

def main():
    """Main function to collect emails and names and display them."""
    email_to_name = {}
    email = input ("Enter your email:")
    while email != "":
        guessed_name = extract_name_from_email (email)
        confirmation = input (f"Is your name {guessed_name}? (y/n)").lower ()
        if confirmation != "" and confirmation != "y":
            name = input ("Enter your name:")
        else:
            name = guessed_name

        email_to_name[email] = name
        email = input ("Enter your email:")

    print ()
    for email, name in email_to_name.items():
        print (f"{name} ({email})")



def extract_name_from_email(email):
    """Extract a guessed name from an email address."""
    username = email.split("@")[0]
    parts = username.split(".")
    name = "".join(parts)
    return name

main()


