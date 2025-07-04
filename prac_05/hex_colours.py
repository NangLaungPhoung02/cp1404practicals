""" Hex  colour lookup
Estimate : 15 minutes
Actual: 35 minutes """

COLOUR_TO_HEX = {"Absolute Zero": "#0048ba",
                 "Acid Green": "#b0bf1a",
                 "Alice Blue": "#f0f8ff",
                 "Alizarin crimson": "#e32636",
                 "Amaranth": "#e52b50",
              "Amber":"#ffbf00",
                 "Amethyst": "#9966cc",
                 "AntiqueWhite": "faebd7",
                 "Aqua":"#00ffff",
                 "Army Green": "#4b5320"}

colour_name = input("Enter colour name:").strip().title()
while colour_name !="":
    try:
        print (f"{colour_name} colour code is {COLOUR_TO_HEX[colour_name]}")
    except KeyError:
        print ("Invalid colour name")
    colour_name = input("Enter colour name:").strip().title()

