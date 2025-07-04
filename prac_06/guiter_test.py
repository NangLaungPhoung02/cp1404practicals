"""
guitar_test.py
Estimate time:40 minutes
Actual total three file of guitar: 1 hour
"""

from guitar import Guitar

def main():
    """Test the guitar class methods."""
    guitar1 = Guitar ("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar ("Line 6 JTV-59", 2010, 1512.9)

    print(f"{guitar1.name} get_age() - Expected 102. got{guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected 11. got{guitar2.get_age()}")

    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False.Got {guitar2.is_vintage()}")


main()
