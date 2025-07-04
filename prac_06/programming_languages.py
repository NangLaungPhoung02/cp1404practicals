"""
Programming languages.py
Estimate : 30 minutes
Actual  total 2 files times: 50 minutes
"""

class ProgrammingLanguages:
    """Represents a programming language with typing, reflection and year introduced. """
    def __init__(self, name, typing, reflection, year):
        """ Initialize a programming language instance,"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return true if the language uses dynamic typing. """
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """ Return s string representation of the language."""
        return f"{self.name}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}"

