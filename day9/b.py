numberVector = []
with open("day9/input", "r") as inputFile:
    for line in inputFile:
        numberVector.append(int(line))

interestingNumber = 375054920

for index, number in enumerate(numberVector):
    sum = number
    for index2, consecutiveNumber in enumerate(numberVector):
        if index2 <= index:
            continue

        sum += consecutiveNumber
        
        if sum == interestingNumber:
            print(f"last number in correct sequence: {consecutiveNumber}")
            print("sequence:")
            [print(x) for x in numberVector[index:index2 + 1]]
            smallest = min(numberVector[index:index2 + 1])
            largest = max(numberVector[index:index2 + 1])
            print(f"smallest: {smallest} largest: {largest} sum: {smallest + largest}")
            break
        elif sum > interestingNumber:
            break

    if sum == interestingNumber:
        print(f"first number in correct sequence: {number}")
        print(f"first + last = {number + consecutiveNumber}")
