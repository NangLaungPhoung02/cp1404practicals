password = '<PASSWORD>'
def main():
    password = input ("Enter password:")
    print (is_valid_password(password))

def is_valid_password (password):
    """Determine if password is considered valid."""
    if len(password) < 6 or "" in password:
        return False
    return True


main()
