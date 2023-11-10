class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        current_year = 2022
        age = current_year - self.year
        print(f"In {current_year} the {self.name} is: {age}")
        return age, current_year

    def is_vintage(self, age):
        if age >= 50:
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        return vintage_string

    def __str__(self, vintage_string):
        return f"{self.name} ({self.year}) : ${self.cost}{vintage_string}"
