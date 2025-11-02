"""
CP1404 prac 5
HEX COLOURS task
Look up hexadecimal colour codes by name.
"""
COLOUR_CODES = {
    "aqua": "#00ffff",
    "alizarin": "#e32636",
    "baby blue": "#89cff0",
    "baby pink": "#f4c2c2",
    "barn red": "#7c0a02",
    "chartreuse": "#bfff00",
    "black": "#000000",
    "bright green": "#66ff00",
    "candy apple red": "#ff0800",
    "canary yellow": "#ffff99"
}


colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    if colour_name in COLOUR_CODES:
        print(f"{colour_name.title()} is {COLOUR_CODES[colour_name]}")
        colour_name = input("Enter a colour name: ").lower()
    else:
        print("Invalid colour name.")
        colour_name = input("Enter a colour name: ").lower()
print("Goodbye!")
