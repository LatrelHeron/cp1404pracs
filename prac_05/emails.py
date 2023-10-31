"""
Word Occurrences
Estimate: 25 minutes
Actual:   took breaks in between undetermined
"""


def main():
    """Get email and name for a user and once completed display all names with corresponding email"""
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
    """Extracte name based on where the @ character is in string"""
    name = email.split('@')[0]
    name_parts = name.split('.')
    name = ' '.join([part.title() for part in name_parts])
    return name


main()
