"""
Project Management
Estimate: 60 minutes
Actual:    minutes
"""
import datetime

from prac_07.project import Project

FILENAME = "projects.txt"
MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")

def main():
    """Pythonic Project Management Program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)

def load_projects(filename):
    """Load projects from file."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects

def save_projects(filename, projects):
    """Save projects to file."""
    with open(filename, "w") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(f"{project.save_string()}\n")

def display_projects(projects):
    """Display complete and incomplete projects sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])
    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects:")
    for p in complete:
        print(f"  {p}")

def filter_projects_by_date(projects):
    """Ask the user for a date and display only projects that start after that date, sorted by date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered = sorted([p for p in projects if p.start_date >= filter_date], key=lambda p: p.start_date)
    for p in filtered:
        print(p)

def add_project(projects):
    """Ask the user for the inputs and add a new project"""
    print("Let's add a new project")
    name = input("Name: ")
    date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    precent = int(input("Precent complete: "))
    projects.append(Project(name, date, priority, cost, precent))

def update_project(projects):
    """Update existing projects."""
    for i , project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    project = projects[project_choice]
    print(project)
    new_percentage = input("New percentage: ")
    if new_percentage:
        project.completion_percentage = int(new_percentage)
    new_priority = input("New priority: ")
    if new_priority:
        project.priority = int(new_priority)

main()