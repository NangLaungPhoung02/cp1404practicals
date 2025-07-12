"""
guitars.py
Estimate time 30 minutes
Actual total three files time: 50 minutes
"""

from datetime import datetime

CURRENT_YEAR = datetime.now().year

class Guitar:
    """ Represents the guitar objects."""
    def __init__(self, name="", year = 0, cost = 0):
        """Initialize a guitar instance with name, year and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """ Return the age of the guitars in years. """
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is more 50 or more years old. """
        return self.get_age()>= 50

    def __lt__(self,other):
        """sort guitars by year."""
        return self.year < other.year
