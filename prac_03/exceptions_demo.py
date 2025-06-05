"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

#1. What will a ValueError occur?
    #Numerator and denominator must be valid numbers!

#2. When will a ZeroDivisionError occur?
    #Cannot divide by zero!

#3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    #If denominator is zero, it prints a message and does not attempt the division, so no ZeroDivisionError will occur.