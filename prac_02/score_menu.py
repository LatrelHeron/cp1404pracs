def main():
    MENU = """Menu: 
(G)et score
(P)rint result
(S)how stars
(Q)uit"""
    print(f"{MENU}")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice, renter choice")
        print(f"{MENU}")
        choice = input(">>> ").upper()
    print("farewell")


def get_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    print("*" * score)


main()