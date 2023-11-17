from prac_07.project import Project
import datetime

def main():
    file_name = 'projects.txt'
    projects = load_project(file_name)
    print("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit\n")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_project()
        elif choice == "S":
            save_project(projects)
        elif choice == "D":
            display_project()
        elif choice == "F":
            filter_project()
        elif choice == "A":
            add_project()
        elif choice == "U":
            update_project()
        else:
            print("Invalid choice, renter choice")
        print("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit\n")
        choice = input(">>> ").upper()


def load_project(file_name):
    projects = []
    in_file = open(file_name, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        project = Project(parts[0], parts[1], parts[2], parts[3], parts[-1])
        projects.append(project)
    in_file.close()
    projects.sort()
    return projects


def save_project(projects, file_name):
    out_file = open(file_name, 'w')
    for project in projects:
        out_file.write(f"{name}, {start_date}, {priority}, {cost_estimate}, {percentage}")
    out_file.close()


def display_project(projects):
    for project in projects:
        print(project)




def filter_project():
    filter_date = input("Date (d/m/yyyy): ")
    date = datetime.datetime.striptime(filter_date, "%d/%m/%Y")


def add_project(projects):
    name = input("Name: ")
    start_date = input("Date (d/m/yyyy): ")
    date = datetime.datetime.striptime(start_date, "%d/%m/%Y")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    percentage = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, percentage)
    projects.append(new_project)



def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {projects[0]}, start: {projects[1]}, priority {projects[2]}, estimate: ${projects[3]}, completion: {projects[-1]}%")
    project_choice = input("Project choice: ")
    if 0 <= project_choice < len(projects):
        project = projects[project_choice]
        new_percentage = int(input("New Percentage: "))
        if new_percentage <= 0 or new_percentage > 100:
            print("Invalid percentage, range must be between 0 to 100")
    else:
        print("Invalid project")

if __name__ == "__main__":
    main()



