# @author cody
# @date 2022.03.07
#
# coding plan
# 	copy asm files over
# 	read a file → output same file
# 		use f-strings, e.g. print(f"{line}")
# 	ignore whitespace
# 	ignore full-line comments
# 	ignore mid-line comments
#
# intermediate coding plan:
#
#
#
#
#

#
#  definitions borrowed from Winry's project
#
import string
import math


class Parser:
    def __init__(self):
        self.compDict = {
            "0": "0101010",
            "1": "0111111",
            "-1": "0111010",
            "D": "0001100",
            "A": "0110000",
            "M": "1110000",
            "!D": "0001101",
            "!A": "0110001",
            "!M": "1110001",
            "-D": "0001111",
            "-A": "0110011",
            "-M": "1110011",
            "D+1": "0011111",
            "A+1": "0110111",
            "M+1": "1110111",
            "D-1": "0001110",
            "A-1": "0110010",
            "M-1": "1110010",
            "D+A": "0000010",
            "D+M": "1000010",
            "D-A": "0010011",
            "D-M": "1010011",
            "A-D": "0000111",
            "M-D": "1000111",
            "D&A": "0000000",
            "D&M": "1000000",
            "D|A": "0010101",
            "D|M": "1010101"
        }

        self.destDict = {
            "null": "000",
            "M": "001",
            "D": "010",
            "MD": "011",
            "A": "100",
            "AM": "101",
            "AD": "110",
            "AMD": "111",
        }

        self.jumpDict = {
            "null": "000",
            "JGT": "001",
            "JEQ": "010",
            "JGE": "011",
            "JLT": "100",
            "JNE": "101",
            "JLE": "110",
            "JMP": "111",
        }


parser = Parser()


def decimal_to_binary(num):
    # the result that we're going to return starts at an empty list
    binary_result = []

    # we're going to modify n, so let's make a copy
    number = int(num)

    # as long as the length of the result is less than 15...
    while len(binary_result) < 15:
        binary_result.insert(0, number % 2)
        number = math.floor(number / 2)

    return binary_result


assemblyFile = open("asm/Max.asm", "r")
output = open("asm/MaxCody.hack", "w")

# let's define our symbol table, used for finding labels and variables
symbolTable = {
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "R0": 0,
    "SCREEN": 16384,
    "KBD": 24576,
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4
}

# we've added our pre-defined symbols, so now we should move on to our first pass, adding our labels.
linesPassed = 0
for code in assemblyFile:
    # omg we'll have to modify this string a lot. " ".join(code.split()) will remove newline characters, and .replace(" ", "") will remove all whitespaces.
    linePartOne = " ".join(code.split()).replace(" ", "")
    try:
        indexOfAComment = linePartOne.index('/')
    except ValueError:
        indexOfAComment = 0
    line = linePartOne
    if indexOfAComment:
        line = linePartOne[0:indexOfAComment]

    if len(line) > 0 and line[0] == "(":
        symbolTable[line[1:-1]] = linesPassed
    elif len(line) > 0 and line[0] != string.whitespace and code[0] != "/":
        linesPassed += 1

assemblyFile.close()

assemblyFile = open("asm/Max.asm", "r")

# we've done our first pass, so now we should move on to our second pass, adding our variables.
n = 16
for code in assemblyFile:
    # omg we'll have to modify this string a lot. " ".join(code.split()) will remove newline characters, and .replace(" ", "") will remove all whitespaces.
    linePartOne = " ".join(code.split()).replace(" ", "")
    try:
        indexOfAComment = linePartOne.index('/')
    except ValueError:
        indexOfAComment = 0
    line = linePartOne
    if indexOfAComment:
        line = linePartOne[0:indexOfAComment]

    if len(line) > 0 and line[0] == "@":
        try:
            ignoreMePlease = int(line[1:])
        except ValueError:
            if symbolTable.get(line[1:]) is None:
                symbolTable[line[1:]] = n
                n += 1

print(symbolTable)

assemblyFile.close()


assemblyFile = open("asm/Max.asm", "r")

counter = 0
for code in assemblyFile:
    # omg we'll have to modify this string a lot. " ".join(code.split()) will remove newline characters, and .replace(" ", "") will remove all whitespaces.
    linePartOne = " ".join(code.split()).replace(" ", "")
    try:
        indexOfAComment = linePartOne.index('/')
    except ValueError:
        indexOfAComment = 0
    line = linePartOne
    if indexOfAComment:
        line = linePartOne[0:indexOfAComment]

    print(line)

    # is this whitespace or not? If not, then we should translate our instruction.
    if len(line) > 1 and line[0] != '/' and line[0] != ' ' and line[0] != "(":
        # our finished translation
        translation = ""
        # is it an A instruction or a C instruction
        if line[0] == "@":
            # it is an A-instruction! we add the opcode, 0, add the result, and for each bit, we add the string translation of the bit
            translation += "0"
            try:
                result = decimal_to_binary(line[1:])
            except ValueError:
                result = decimal_to_binary(symbolTable[line[1:]])

            for bit in result:
                translation += str(bit)
        else:
            # it's a C-instruction!
            # add the opcode
            translation += "111"
            # destination
            destinationIndex = -1
            addDest = True
            try:
                destinationIndex = line.index("=")

            # but what happens if there isn't? then it'll throw a ValueError.
            except ValueError:
                translation += "000"
                addDest = False

            # jump
            jumpIndex = len(line)
            addJump = True
            try:
                jumpIndex = line.index(";")

            # but what happens if there isn't? then it'll throw a ValueError
            except ValueError:
                translation += "000"
                addJump = False

            # the comp can't be zero, and I'm adding it in the correct order
            translation += parser.compDict[line[destinationIndex+1:jumpIndex]]

            # the destination index is the destination end and 0 is the start, and we don't need that if we're taking substrings here.
            if addDest:
                translation += parser.destDict[line[:destinationIndex]]

            # `jumpIndex` is the jump start and the file's length is the end, and we don't need that if we're taking substrings here.
            if addJump:
                translation += parser.jumpDict[line[jumpIndex + 1:]]

        print(f"{counter}: {line}, {translation}")
        output.write(translation + "\n")

    counter += 1
    # pass

assemblyFile.close()
output.close()
