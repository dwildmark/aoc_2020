import re

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
        valid = True
        if not (self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid):
            return False
        
        if int(self.byr) < 1920 or int(self.byr) > 2002:
            valid = False
        
        if int(self.iyr) < 2010 or int(self.iyr) > 2020:
            valid = False

        if int(self.eyr) < 2020 or int(self.eyr) > 2030:
            valid = False

        if "cm" in self.hgt:
            height = self.hgt.strip("cm")
            if int(height) < 150 or int(height) > 193:
                valid = False
        elif "in" in self.hgt:
            height = self.hgt.strip("in")
            if int(height) < 59 or int(height) > 76:
                valid = False
        else:
            valid = False

        if not re.search(r'^#[0-9a-f]{6}$', self.hcl):
            valid = False

        if not re.search(r'(amb|blu|brn|gry|grn|hzl|oth)$', self.ecl):
            valid = False

        if not re.search(r'^[0-9]{9}$', self.pid):
            valid = False

        return valid 

    def setField(self, fieldString, fieldValue):
        if ("byr" == fieldString):
            self.byr = fieldValue 
        elif ("iyr" == fieldString):
            self.iyr = fieldValue 
        elif ("eyr" == fieldString):
            self.eyr = fieldValue 
        elif ("hgt" == fieldString):
            self.hgt = fieldValue
        elif ("hcl" == fieldString):
            self.hcl = fieldValue
        elif ("ecl" == fieldString):
            self.ecl = fieldValue
        elif ("pid" == fieldString):
            self.pid = fieldValue
        elif ("cid" == fieldString):
            self.cid = fieldValue
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
            currentPassport.setField(pair.split(":")[0], pair.split(":")[1])
        
    print(f'Number of valid passports: {validPassports}')

