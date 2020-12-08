with open("day3/input", "r") as inputFile:
    xIndex = 0
    treesHit = 0
    for line in inputFile:
        modifiedLine = list(line)
        if line[xIndex] == '#':
            treesHit += 1
            modifiedLine[xIndex] = "X"
        else:
            modifiedLine[xIndex] = "O"
        
        print("".join(modifiedLine))
        xIndex += 3
        xIndex %= len(line) - 1

    print(treesHit)
