"""
CP1404 prac 5
HEX COLOURS task
"""
colour_codes = {
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

"""Look up hexadecimal colour codes by name."""
colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    if colour_name in colour_codes:
        print(f"{colour_name.title()} is {colour_codes[colour_name]}")
        colour_name = input("Enter a colour name: ").lower()
    else:
        print("Invalid colour name.")
        colour_name = input("Enter a colour name: ").lower()
print("Goodbye!")
