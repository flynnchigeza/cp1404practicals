"""CP140 4Prac 07 - Project class for project management system.

Estimated time: 20 mins
Actual time 40 mins

Defines the Project class with attributes for name, start date, priority,
cost estimate, and completion percentage. Provides comparison functionality
for sorting by priority and helper methods for displaying and checking
completion status.
"""

from datetime import date


class Project:
    """Represent a project with key attributes and utility methods."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date  # datetime.date object
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a nicely formatted string representation of a Project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Define less-than comparison based on project priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if the project is fully complete."""
        return self.completion_percentage == 100

    def starts_after(self, date_filter):
        """Return True if the project's start date is after the given date."""
        return self.start_date > date_filter