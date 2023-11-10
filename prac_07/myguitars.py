"""
My Guitars Prac 7
"""
from prac_07.guitar import Guitar


def main():
    """
    Read file of guitars, store them in list and sort by year
    Program to get users new guitars and store in guitars.csv
    """
    guitars = load_guitar()
    get_guitar(guitars)


def load_guitar():
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    return guitars


def get_guitar(guitars):
    name = input("Name of guitar: ").capitalize()
    while name != "":
        year = int(input("Year guitar was made: "))
        cost = float(input("Cost of guitar in $: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        name = input("Name of guitar: ").capitalize()
    save_guitars(guitars)


def save_guitars(guitars):
    out_file = open('guitars.csv', 'w')
    for guitar in guitars:
        out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    out_file.close()


main()
