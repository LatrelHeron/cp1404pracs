def main():
    data = read_wimbledon_data("wimbledon.csv")
    champions = count_champions(data)
    countries_of_champions = get_countries_of_champions(data)
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")
    print(f"\nThese {len(countries_of_champions)} countries have won Wimbledon:")
    print(", ".join(countries_of_champions))


def read_wimbledon_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()
        for line in lines:
            fields = line.strip().split(',')
            data.append(fields)
    return data


def count_champions(data):
    champions = {}
    for entry in data:
        champion = entry[2]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def get_countries_of_champions(data):
    countries = set()
    for entry in data:
        countries.add(entry[1])
        countries.add(entry[3])
    return sorted(countries)


main()
