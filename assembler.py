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

print(assemblyFile.read())

assemblyFile.close()

