array = []

with open("day1/input", "r") as inputFile:
    for line in inputFile:
        array.append(int(line))

array.sort()

for numberA in array:
    for numberB in array:
        for numberC in array:
            if numberA + numberB + numberC == 2020:
                print(f'{numberA} * {numberB} * {numberC} = {numberA * numberB * numberC}')
                break