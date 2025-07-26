"""
project.py
Estimate time  : 1 hour
Actual total three files time:  1 and half hour
"""

from datetime import datetime
class Project:
    """Represent a project with name, start date, priority, cost estimate and completion %."""
    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.percent_complete = int(percent_complete)

    def is_complete(self):
        """Return True if project is 100% complete."""
        return self.percent_complete == 100

    def __lt__(self,other):
        """Support sorting by priority."""
        return self.priority < other.priority

    def __str__(self):
        """Return the presentation by the project."""
        return (f"{self.name}, start: {self.start_date.strftime ('%d/%m/%Y')},"
                f"priority: {self.priority}, estimate:${self.cost_estimate:.2f},"
                f"Completion: {self.percent_complete}%")

    def to_tab_delimited(self):
        """Convert project to tab_delimited string format for saving."""
        return f"{self.name}\t{self.start_date.strftime ('%d/%m/%Y')}\t{self.priority}\t{self.cost_estimate}\t{self.percent_complete}"

