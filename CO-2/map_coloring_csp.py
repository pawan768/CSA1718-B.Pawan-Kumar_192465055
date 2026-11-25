# Map Coloring using Constraint Satisfaction Problem (CSP)
colors = ["Red", "Green", "Blue"]
neighbors = {
    "A": ["B", "C"], "B": ["A", "C", "D"],
    "C": ["A", "B", "D"], "D": ["B", "C"]
}
assignment = {}

def is_safe(region, color):
    return all(assignment.get(n) != color for n in neighbors[region])

def solve():
    if len(assignment) == len(neighbors):
        return True
    region = next(r for r in neighbors if r not in assignment)
    for color in colors:
        if is_safe(region, color):
            assignment[region] = color
            if solve():
                return True
            del assignment[region]
    return False

if solve():
    print("Map coloring solution:")
    for region, color in assignment.items():
        print(region, ":", color)
else:
    print("No solution exists.")
