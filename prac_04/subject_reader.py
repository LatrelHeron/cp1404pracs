"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    print(f"{subject} is taught by {lecturer} and has {number_of_students}")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    parts = []
    with open(FILENAME, 'r') as input_file:
        for line in input_file:
            line = line.strip()  # Remove the \n
            data = line.split(',')  # Separate the data into its parts
            if len(data) == 3:
                subject, lecturer, number_of_students = data
                # Stores data for each column in parts list
                parts.append([subject.strip(), lecturer.stip(), int(number_of_students())])
    return parts


main()
