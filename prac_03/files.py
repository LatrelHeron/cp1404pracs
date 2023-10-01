#1.Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it. Remember to close your file. = "name.txt"
NAMES = "name.txt"
name = input("Name: ")
out_file = open(NAMES, 'w')
print(name, file=out_file)
out_file.close()

#2. Write code that opens "name.txt" and reads the name (as above) then prints, "Your name is Bob"
NAMES = "name.txt"
in_file = open(NAMES)
name = in_file.read()
in_file.close()
print("Your name is", name)

#3. Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result, which should be... 59.
NUMBERS = "numbers.txt"
in_file = open(NUMBERS, "r")
line1 = int(in_file.readline().strip())
line2 = int(in_file.readline().strip())
result = line1 + line2
print(result)
in_file.close()

#4.
NUMBERS = "numbers.txt"
in_file = open(NUMBERS, "r")
for line in in_file:
    print(line.strip())
in_file.close()
