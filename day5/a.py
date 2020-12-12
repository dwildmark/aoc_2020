import re

def getRowIndex(rowString):
    minIndex = 0
    maxIndex = 127
    for char in rowString:
        if char == 'F':
            maxIndex = minIndex + (maxIndex - minIndex) // 2
        else:
            minIndex = maxIndex - (maxIndex - minIndex) // 2
    
    assert(minIndex == maxIndex)
    return maxIndex

def getColIndex(colString):
    minIndex = 0
    maxIndex = 7
    for char in colString:
        if char == 'L':
            maxIndex = minIndex + (maxIndex - minIndex) // 2
        else:
            minIndex = maxIndex - (maxIndex - minIndex) // 2
    
    assert(minIndex == maxIndex)
    return maxIndex

with open("day5/input", "r") as inputFile:
    boardingPasses = []
    for index, line in enumerate(inputFile):
        rowPatternString = re.search(r'^(F|B){7}', line)[0]
        colPatternString = re.search(r'(R|L){3}$', line)[0]
        rowIndex = getRowIndex(rowPatternString)
        colIndex = getColIndex(colPatternString)

        boardingPasses.append({
            "row": rowIndex,
            "col": colIndex,
            "id": (rowIndex * 8 + colIndex)
        })
    
    boardingPassesSortedByRow = sorted(boardingPasses, key=lambda boardingPass: boardingPass["id"])
    minRow = boardingPassesSortedByRow[0]["row"]
    maxRow = boardingPassesSortedByRow[-1]["row"]
    for row in range(minRow, maxRow):
        rowString = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        inThisRow = [x for x in boardingPassesSortedByRow if x["row"] == row]
        for bp in inThisRow:
            rowString[bp["col"]] = 'X'
        print("".join(rowString))