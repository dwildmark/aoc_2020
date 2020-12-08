validPasswords = 0
with open("day2/input", "r") as inputFile:
    for line in inputFile:
        lineParts = line.split(":")
        rulePart = lineParts[0].split(" ")
        password = lineParts[1].strip(" ")
        counts = rulePart[0].split("-")
        indexA = int(counts[0]) - 1
        indexB = int(counts[1]) - 1
        letter = rulePart[1]

        if (password[indexA] == letter and not password[indexB] == letter) or (not password[indexA] == letter and password[indexB] == letter):
            validPasswords += 1

print(validPasswords)