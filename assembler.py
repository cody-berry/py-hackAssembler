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

import math

def decimal_to_binary(n):
    # the result that we're going to return starts at an empty list
    result = []

    # we're going to modify n, so let's make a copy
    number = int(n)

    # as long as the length of the result is less than 15...
    while len(result) < 15:
        result.insert(0, number % 2)
        number = math.floor(number/2)

    return result


assemblyFile = open("asm/MaxL.asm", "r")

counter = 0
for code in assemblyFile:
    # omg we'll have to modify this string a lot. " ".join(code.split()) will remove newline characters, and .replace(" ", "") will remove all whitespaces.
    line = " ".join(code.split()).replace(" ", "")

    # is this whitespace or not? If not, then we should translate our instruction.
    if (len(line) > 1 and line[0] != '/' and line[0] != ' '):
        # our finished translation
        translation = ""
        # is it an A instruction or a C instruction
        if line[0] == "@":
            translation += "0"
            result = decimal_to_binary(line[1:])
            for bit in result:
                translation += str(bit)



        print(f"{counter}: {line}, {translation if line[0] == '@' else 'C'}")
    counter += 1


assemblyFile.close()



