"""
CP1404 Prac 07 - More Guitars
Read, display, sort, and save a list of Guitar objects.

"""

from guitar import Guitar


FILENAME = 'guitars.csv'


def main():
    """Read guitars from file, display, add new ones, and save."""
    guitars = load_guitars(FILENAME)
    display_guitars(guitars, title="Guitars loaded:")

    # Add new guitars from user input
    guitars += get_new_guitars()

    # Sort guitars by year (using __lt__)
    guitars.sort()
    display_guitars(guitars, title="Sorted guitars:")

    # Save updated list to file
    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    """Load guitars from a CSV file into a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars, title="Guitars:"):
    """Display all guitars in a formatted list."""
    print(title)
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar} {vintage_string}")
    print()


def get_new_guitars():
    """Prompt user to enter new guitars."""
    print("Add new guitars (press Enter to stop):")
    guitars = []
    name = input("Name: ").strip()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
        name = input("Name: ").strip()
    return guitars





if __name__ == '__main__':
    main()