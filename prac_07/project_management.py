"""
project management.py
Estimate time  : 1 hour
Actual total three files time:  1 and half hour
"""
from project import Project
from datetime import datetime

FILENAME = "project.txt"
def main():
    """"""
    projects = load_project(FILENAME)
    print ("Welcome to pythonic project management")
    print (f"Loaded{len(projects)} projects from {FILENAME}")
    display_menu()
    choice = input(">>>").lower()
    while choice != "q":
        if choice == "L":
            filename = input("Enter filename to load:")
            project = load_project(filename)
        elif choice =="S":
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            date_string = input("Show project that start after date (dd/mm/yy)")
            filter_projects_by_date (projects, date_string)
        elif choice == "A":
            new_project = add_new_project()
            projects.append(new_project)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid option.")
        choice = input(">>>").lower()
    save_choice = input(f"Would you like to save to {FILENAME}?").lower()
    if save_choice in("yes", "y"):
        save_projects(FILENAME, projects)
    print ("Thank you for using project management. ")


def load_project(filename):
    """Load project objects from a tab-delimited file, skipping the header."""
    projects=[]
    try:
        with open(filename) as file:
            next(file)
            for line in file:
                parts = line.strip().split('\t')
                name, start_date, priority, cost_estimate, percent_complete = parts
                projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))
    except FileNotFoundError:
        print("File not found")
    return projects

def display_menu():
    """Display menu option to the user."""
    print("Menu:\n L- Load projects \n S-Save projects \n D-Displayed projects\nF-Filter projects by date\nA-Add new project \nU-Update project \nQ-Quit")

def save_projects(filename, projects):
    """Save the list of project to a tab-delimited file."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(project.to_tab_delimited() + "\n")

def display_projects(projects):
    """Display incomplete and complete projects separately, sorted by priority."""
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [ p for p in projects if p.is_complete()]

    print ("Incomplete projects:")
    for project in sorted(incomplete):
        print(f"{project}")

    print("Complete projects:")
    for project in sorted(complete):
        print (f"{project}")

def filter_projects_by_date(projects, input_date_str):
    """Display projects starting after the given date, sorted by start date. """
    try:
        input_date = datetime.strptime(input_date_str, "%d/%m/%Y").date()
        filtered = [p for p in projects if p.start_date > input_date]
        filtered.sort(key=lambda p:p.start_date)
        for project in filtered:
            print(project)
    except ValueError:
        print("Invalid date.")

def add_new_project():
    """Prompt user for project details and return a new project."""
    print("Add new project:")
    name = input("Add new project name:")
    start_date = input("Add new project start date(dd/mm/yy:")
    priority = input("Add new project priority:")
    cost_estimate = input("Add new project cost estimate:")
    percent_complete = input("Add new project percent complete:")
    return Project(name, start_date, priority, cost_estimate, percent_complete)

def update_project(projects):
    """Update the completion percentage and/or priority of a selected project. """
    for i, project in enumerate(projects):
        print(f"{i}{project}")
    try:
        choice = int(input("Choose an option:"))
        selected = projects[choice]
        print(selected)
        new_percent = input("New Percentage:")
        new_priority = input("New Priority:")

        if new_percent :
            selected.percent_complete = int(new_percent)
        if new_priority:
            selected.priority = int(new_priority)

    except (ValueError, IndexError):
        print("Invalid selection.")

main()



