"""
my guitars.py
Estimate time 40 minutes
Actual total three files time:  50 minutes
"""
import csv
from guitar import Guitar
FILENAME = "guitars.csv"

def main():
    """Get guitar data from user and display formatted list."""
    guitars = load_guitars (FILENAME)
    display_guitars(guitars)

    new_guitars = add_user_guitars()
    guitars.extend(new_guitars)

    guitars.sort()

    print("\nSorted guitars:")
    display_guitars(guitars)

    save_guitars (FILENAME, guitars)
    print (f"\nGuitars saved to {FILENAME}")

def load_guitars (filename):
    """Loading the guitars from csv file and return a list of guitar objects"""
    guitars = []
    try:
        with open (filename, "r", newline = '', encoding = "uft-8") as in_file:
            reader = csv.reader(in_file)
            for row in reader:
                name, year, cost = row
                guitars.append(Guitar(name.strip(), int(year), float(cost)))
    except FileNotFoundError:
        print("No existing data file")
    return  guitars


def display_guitars(guitars):
    """Print a formatted list of guitars, showing name, year and cost, vintage status."""
    print ("\n These are my guitars:")
    for i, guitar in enumerate (guitars, 1):
        vintage_str = "(vintage)" if guitar.is_vintage() else""
        print (f"Guitar {i} : {guitar.name:>30} ({guitar.year}), worth $ {guitar.cost : 10,.2f}{vintage_str}")

def add_user_guitars():
    """Prompt the user to add new guitars and return a list of them."""
    new_guitars = []
    print("\nAdd new guitars:")
    name = input("Guitar Name:")
    while name:
        year = int(input("Year:"))
        cost = float(input("Cost:"))
        new_guitars.append (Guitar (name, year, cost))
        name = input("Guitar Name:")
    return new_guitars

def save_guitars(filename, guitars):
    """ Write the list of guitar object to a CSV file."""
    with open (filename, "w", newline = '', encoding = "uft-8") as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

main()