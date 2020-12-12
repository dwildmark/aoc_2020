with open("day6/input", "r") as inputFile:
    sum = 0
    memberCount = 0
    answeredQuestions = dict()
    for line in inputFile:
        print(sorted(line.strip("\n")))
        if line == "\n":
            for key, value in answeredQuestions.items():
                if value == memberCount:
                    sum += 1
            print(sum)
            answeredQuestions = dict()
            memberCount = 0
            continue
        
        memberCount += 1
        for char in line.strip("\n"):
            if char in answeredQuestions:
                answeredQuestions[char] += 1
            else:
                answeredQuestions[char] = 1
        
    print(sum)