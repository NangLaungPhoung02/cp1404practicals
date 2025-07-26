"""
guitars.py
Estimate time 40 minutes
Actual total three files time: 1 hour
"""

from guitar import Guitar

def main():
    """Get guitar data from user and display formatted list."""

    print ("My guitars:")
    guitars=[]
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
    guitars.append(Guitar("Gibson L-5 CSE", 1992, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))

    print ("\nThese are my guitars:")
    for i, guitar in enumerate (guitars, 1):
        vintage_str = "(vintage)" if guitar.is_vintage() else""
        print (f"Guitar {i} : {guitar.name:>20} ({guitar.year}), worth $ {guitar.cost : 10,.2f}{vintage_str}")


main()
