"""
get password.
password length must be at least 10 characters long to be valid
for every character in password display *
"""
length_of_password = 0
password = input("Password: ")
print(len(password))
"""while length_of_password < 10:
    print("Invalid length of password")
    password = input("Password: ")
for j in range(length_of_password):
    print(end="*")"""
