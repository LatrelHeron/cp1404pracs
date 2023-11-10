from prac_06.guitar import Guitar

test_guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
test_guitar2 = Guitar("Another Guitar", 2013, 1200.50)

print(f"{test_guitar1.name} get_age() - Expected 100. Got {test_guitar1.get_age()}")
print(f"{test_guitar2.name} get_age() - Expected 9. Got {test_guitar2.get_age()}")

print(f"{test_guitar1.name} is_vintage() - Expected True. Got {test_guitar1.is_vintage()}")
print(f"{test_guitar2.name} is_vintage() - Expected False. Got {test_guitar2.is_vintage()}")