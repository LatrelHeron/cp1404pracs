import random

minimum_number = 1
maximum_number = 45
quick_picks = int(input("How many quick picks? "))
for i in range(quick_picks):
    number_generator = sorted(random.sample(range(minimum_number, maximum_number + 1), 6))
    print(" ".join(map(str, number_generator)))

