array = []

with open("day1/input", "r") as inputFile:
    for line in inputFile:
        array.append(int(line))

array.sort()

for number in array:
    otherNumber = 2020 - number
    if otherNumber in array:
        print(f'{number} * {otherNumber} = {number * otherNumber}')
        break