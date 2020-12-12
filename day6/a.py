with open("day6/input", "r") as inputFile:
    sum = 0
    answeredQuestions = dict()
    for line in inputFile:
        print(sorted(line.strip("\n")))
        if line == "\n":
            print(f'{sorted(answeredQuestions)}, len = {len(answeredQuestions)}')
            sum += len(answeredQuestions)
            print(sum)
            answeredQuestions = dict()
            continue
        
        for char in line.strip("\n"):
            answeredQuestions[char] = ""
        
    print(sum)