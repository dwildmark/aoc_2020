numberVector = []
with open("day9/input", "r") as inputFile:
    for line in inputFile:
        numberVector.append(int(line))

def verify_vector(vector):
    for index, number in enumerate(vector):
        if index < 25:
            continue 

        preambleVector = vector[index - 25 : index]
        preambleDict = {x: "" for x in preambleVector}
        numberValid = False
        print(len(preambleVector))
        for preambleNumber in preambleVector:
            print(f"PreambleNumber: {preambleNumber}")
            if number - preambleNumber == preambleNumber:
                continue

            if (number - preambleNumber) in preambleDict:
                numberValid = True
        
        if not numberValid:
            print(f"At {index}, an invalid number was found: {number}")
            break


verify_vector(numberVector)