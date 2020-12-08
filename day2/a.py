validPasswords = 0
with open("day2/input", "r") as inputFile:
    for line in inputFile:
        lineParts = line.split(":")
        rulePart = lineParts[0].split(" ")
        password = lineParts[1].strip(" ")
        counts = rulePart[0].split("-")
        minCount = int(counts[0])
        maxCount = int(counts[1])
        letter = rulePart[1]
        actualCount = password.count(letter)

        if actualCount <= maxCount and actualCount >= minCount:
            validPasswords += 1

print(validPasswords)