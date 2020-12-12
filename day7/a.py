import re
class Bag:
    def __init__(self, color):
        self.color = color
        self.parents = dict()

    def addParent(self, parent):
        self.parents[parent.color] = parent

bags = dict()

with open("day7/input", "r") as inputFile:
    for line in inputFile:
        parentPart, childrenPart = line.split("contain")
        parent = re.search(r'^[a-z]+ [a-z]+', parentPart)[0]
        children = re.findall(r'[0-9] [a-z]+ [a-z]+', childrenPart)
        # children = [child.strip(" bag") for child in children]
        childrenWithoutNumbers = [re.search(r'[a-z]+ [a-z]+', child)[0] for child in children]
        if parent not in bags:
            bags[parent] = Bag(parent)

        for child in childrenWithoutNumbers:
            if child not in bags:
                bags[child] = Bag(child)

            bags[child].addParent(bags[parent])

bagsContainingShinyGold = dict()
def visit_parents(child):
    bagsContainingShinyGold[child.color] = ''
    for _, value in child.parents.items():
        visit_parents(value)

visit_parents(bags["shiny gold"])

print(len(bagsContainingShinyGold) - 1)