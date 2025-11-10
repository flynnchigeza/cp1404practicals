"""
CP1404 Prac 07 - Project Management System

Estimated time: 40 min
Actual time :1 hours

This module provides a menu-driven program to manage a list of Project
objects. Users can load and save projects from files, display them, filter
by start date, add new projects, and update existing projects.
Demonstrates file I/O, datetime handling, object-oriented design, sorting,
and menu-based user interaction.
"""

from datetime import datetime
from project import Project

DEFAULT_FILENAME = "projects.txt"
DATE_FORMAT = "%d/%m/%Y"


def main():
    """
    Run the Project Management program.

    Loads projects from the default file, displays a menu for user actions,
    and allows loading/saving, filtering, adding, and updating projects.
    """
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    menu = (
        "- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit"
    )

    choice = input(menu + "\n>>> ").lower()
    while choice != "q":
        if choice == "l":
            filename = input("Enter filename to load from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Enter filename to save to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid choice")
        choice = input(menu + "\n>>> ").lower()

    save_choice = input(f"Would you like to save to {DEFAULT_FILENAME}? ").lower()
    if save_choice in ("y", "yes"):
        save_projects(DEFAULT_FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """
    Load projects from a tab-delimited file.

    Args:
        filename (str): The path to the file to load.

    Returns:
        list[Project]: A list of Project objects created from the file.
    """
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split("\t")
            name = parts[0]
            start_date = datetime.strptime(parts[1], DATE_FORMAT).date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def save_projects(filename, projects):
    """
    Save a list of projects to a tab-delimited file.

    Args:
        filename (str): The file to write to.
        projects (list[Project]): The projects to save.
    """
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime(DATE_FORMAT)}\t"
                  f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}", file=out_file)
    print(f"Projects saved to {filename}")


def display_projects(projects):
    """
    Display incomplete and completed projects sorted by priority.

    Args:
        projects (list[Project]): The list of projects to display.
    """
    incomplete_projects = [p for p in projects if not p.is_complete()]
    complete_projects = [p for p in projects if p.is_complete()]
    incomplete_projects.sort()
    complete_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects:")
    for project in complete_projects:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """
    Display projects starting after a specified date.

    Args:
        projects (list[Project]): List of projects to filter.
    """
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(date_string, DATE_FORMAT).date()
    filtered_projects = [p for p in projects if p.starts_after(filter_date)]
    filtered_projects.sort(key=lambda p: p.start_date)
    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    """
    Prompt the user to add a new project.

    Args:
        projects (list[Project]): List to append the new project to.
    """
    print("Let's add a new project")
    name = input("Name: ")
    start_date_string = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.strptime(start_date_string, DATE_FORMAT).date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    """
    Update completion percentage and/or priority of an existing project.

    Args:
        projects (list[Project]): List of projects to choose from.
    """
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)

    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")

    if new_percentage:
        project.completion_percentage = int(new_percentage)
    if new_priority:
        project.priority = int(new_priority)


if __name__ == "__main__":
    main()
