"""
Word Occurrences
Estimate: 25 minutes
Actual:   took breaks in between undetermined
"""


def main():
    user_data = {}
    while True:
        email = input("Email: ")
        if not email:
            break
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm in ['', 'y', 'yes']:
            user_data[email] = name
        else:
            new_name = input("Name: ")
            user_data[email] = new_name
    for email, name in user_data.items():
        print(f"{name} ({email})")


def extract_name(email):
    # Split the email at '@' and take the part before '@'
    name = email.split('@')[0]
    # Split the name by dots and capitalize the first letter of each part
    name_parts = name.split('.')
    name = ' '.join([part.title() for part in name_parts])
    return name


main()
