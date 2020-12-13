import re
import copy
prog = []

with open("day8/input", "r") as inputFile:
    for line in inputFile:
        operation = re.match(r'(acc|jmp|nop)', line).group()
        argument = re.search(r'([+-][0-9]+)', line).group()
        prog.append({"operation": operation, "arg": argument})


def executeProgram(program):
    programCounter = 0
    accumulator = 0

    while(True):
        if programCounter == len(program):
            print("Program exited correctly")
            break
        elif programCounter > len(program):
            print("Program jump out of bounds")
            break

        instruction = program[programCounter]
        if "executed" in instruction:
            print("Program looping")
            break

        if instruction["operation"] == "acc":
            accumulator += int(instruction["arg"])
            programCounter += 1
        elif instruction["operation"] == "jmp":
            programCounter += int(instruction["arg"])
        else:
            programCounter += 1

        instruction["executed"] = True

    return programCounter, accumulator

for index, instruction in enumerate(prog):
    counter = 0
    acc = 0
    programCopy = copy.deepcopy(prog)
    if instruction["operation"] == "nop":
        programCopy[index]["operation"] = "jmp"
        counter, acc = executeProgram(programCopy)
    elif instruction["operation"] == "jmp":
        programCopy[index]["operation"] = "nop"
        counter, acc = executeProgram(programCopy)
    else:
        continue
    
    if counter == len(prog):
        print(f"program ended correctly with programCounter={counter}, accumulator={acc}")
        break
