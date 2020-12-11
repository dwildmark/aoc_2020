class Passport:
    def __init__(self):
        self.byr = False
        self.iyr = False
        self.eyr = False
        self.hgt = False
        self.hcl = False
        self.ecl = False
        self.pid = False
        self.cid = False

    def valid(self):
        return self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid

    def setFieldExisting(self, fieldString):
        if ("byr" == fieldString):
            self.byr = True
        elif ("iyr" == fieldString):
            self.iyr = True
        elif ("eyr" == fieldString):
            self.eyr = True
        elif ("hgt" == fieldString):
            self.hgt = True
        elif ("hcl" == fieldString):
            self.hcl = True
        elif ("ecl" == fieldString):
            self.ecl = True
        elif ("pid" == fieldString):
            self.pid = True
        elif ("cid" == fieldString):
            self.cid = True
        else:
            print(f'Error, fieldString was {fieldString}')

with open("day4/input", "r") as inputFile:
    currentPassport = Passport()
    validPassports = 0
    for line in inputFile:
        if line == "\n":
            # bla bla
            if (currentPassport.valid()):
                validPassports += 1

            currentPassport = Passport()
            continue

        for pair in line.strip("\n").split(" "):
            currentPassport.setFieldExisting(pair.split(":")[0])
        
    print(f'Number of valid passports: {validPassports}')

