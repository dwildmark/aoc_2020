import re
class Bag:
    def __init__(self, color):
        self.color = color
        self.children = dict()

    def addChild(self, child, number):
        self.children[child.color] = {"child": child, "multiplier": number}

bags = dict()

with open("day7/input", "r") as inputFile:
    for line in inputFile:
        parentPart, childrenPart = line.split("contain")
        parent = re.search(r'^[a-z]+ [a-z]+', parentPart).group()
        children = re.findall(r'[0-9] [a-z]+ [a-z]+', childrenPart)
        # childrenWithoutNumbers = [re.search(r'[a-z]+ [a-z]+', child)[0] for child in children]
        if parent not in bags:
            bags[parent] = Bag(parent)

        for child in children:
            childString = re.search(r'[a-z]+ [a-z]+', child).group()
            multiplier = re.match(r'[0-9]', child).group()
            if childString not in bags:
                bags[childString] = Bag(childString)

            bags[parent].addChild(bags[childString], int(multiplier))

shinyGoldContainsBags = 0

def count_child_bags(parent):
    bagSum = 0
    for _, value in parent.children.items():
        bagSum += value["multiplier"]
        bagSum += count_child_bags(value["child"]) * value["multiplier"]
    
    return bagSum

shinyGoldContainsBags = count_child_bags(bags["shiny gold"])

print(shinyGoldContainsBags)