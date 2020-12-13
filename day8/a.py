import re
program = []

with open("day8/input", "r") as inputFile:
    for line in inputFile:
        operation = re.match(r'(acc|jmp|nop)', line).group()
        argument = re.search(r'([+-][0-9]+)', line).group()
        program.append({"operation": operation, "arg": argument})

programCounter = 0
accumulator = 0

while(True):
    instruction = program[programCounter]
    if "executed" in instruction:
        break

    if instruction["operation"] == "acc":
        accumulator += int(instruction["arg"])
        programCounter += 1
    elif instruction["operation"] == "jmp":
        programCounter += int(instruction["arg"])
    else:
        programCounter += 1

    instruction["executed"] = True

print(accumulator)
