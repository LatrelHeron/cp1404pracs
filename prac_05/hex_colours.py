hexadecimals = {"Absolute": "#0048ba", "Acid Green": "", "AliceBlue": "#b0bf1a", "Alizarin crimson": "#f0f8ff",
                "Amaranth": "#e32636", "Amber": "#ffbf00", "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7",
                "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc", }

colour_name = input("Name of colour? ").capitalize()
while colour_name != "":
    if colour_name in hexadecimals:
        print(f"{colour_name}'s code is {hexadecimals[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Name of colour? ").capitalize()
