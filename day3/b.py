with open("day3/input", "r") as inputFile:
    xIndex = 0
    treesHit = 0
    for index, line in enumerate(inputFile):
        if (index % 2 != 0):
            continue

        modifiedLine = list(line)
        if line[xIndex] == '#':
            treesHit += 1
            modifiedLine[xIndex] = "X"
        else:
            modifiedLine[xIndex] = "O"
        
        print("".join(modifiedLine))
        xIndex += 1
        xIndex %= len(line) - 1

    print(treesHit)

    print(211*67*77*89*37)