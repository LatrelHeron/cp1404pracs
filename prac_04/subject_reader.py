"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    # print(f"{subject} is taught by {lecturer} and has {number_of_students}")
    subject_to_data = convert_data(data)
    print(subject_to_data)
    subject = input("What subject code: ")
    print(f"{subject_to_data[subject][0]} teaches {subject}")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])
        data.append(parts)
    input_file.close()
    return data


def convert_data(data):
    subject_to_data = {}
    for subject_data in data:
        subject_to_data[subject_data[0]] = subject_data[1:]
    return subject_to_data


def display_subjects(data):
    """Display data nicely"""
    for subject_data in data:
        print(f"{subject} is taught by {lecturer} and has {number_of_students}")


main()
