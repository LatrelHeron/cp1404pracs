def main():
    password = get_password()
    for i in range(len(password)):
        print(end="*")


def get_password():
    password = input("Password: ")
    while len(password) < 10:
        print("Renter password to meet minimum length of 10 characters")
        password = input("Password: ")
    return password


main()
