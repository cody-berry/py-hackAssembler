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

assemblyFile = open("asm/MaxL.asm", "r")

counter = 0
for code in assemblyFile:
    # omg we'll have to multiply this string a lot. " ".join(code.split()) will remove newline characters, and .replace(" ", "") will remove all whitespaces.
    line = " ".join(code.split()).replace(" ", "")
    print(f"{counter}: {line}, {len(line) > 1 and line[0] != '/' and line[0] != ' '}")
    counter += 1


assemblyFile.close()



