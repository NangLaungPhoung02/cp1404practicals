"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print(f"Result{convert_celsius_to_fahrenheit(celsius):.2f}")

        elif choice == "F":
            fahrenheit = float (input("Fahrenheit:"))
            print (f"Result {convert_fahrenheit_t0_celsius(fahrenheit):.2f}")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def convert_celsius_to_fahrenheit(celsius):
    return celsius *9.0 / 5.0 + 32

def convert_fahrenheit_t0_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 /9

main()