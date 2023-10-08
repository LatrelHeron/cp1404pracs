# Basic list operations
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

total = sum(numbers)
average = total / len(numbers)
minimum = min(numbers)
maximum = max(numbers)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {minimum}")
print(f"The largest number is {maximum}")
print(f"The average of the numbers is {average}")

# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

required_username = input("username: ")
if required_username in usernames:
    print("Access granted")
else:
    print("Access denied")
