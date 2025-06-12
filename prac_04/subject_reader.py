"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details (data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_data =[]
    with open (FILENAME) as input_file:
        for line in input_file:
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            print(parts)  # See what the parts look like (notice the integer is a string)
            parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
            subject_data.append(parts)
            print(parts)  # See if that worked
            print("----------")
    return subject_data

def display_subject_details (data):
    """Display subject details with specific data."""
    for subject, lecture, student_count in data:
        print (f"{subject} is taught by {lecture} and has {student_count} students.")



main()