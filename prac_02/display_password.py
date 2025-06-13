PASSWORD_LENGTH = 8

password = input ("Enter password:")
while len(password) < PASSWORD_LENGTH:
    print ("Invalid password")
    password = input("Enter password:")

print (len(password) * "8")
