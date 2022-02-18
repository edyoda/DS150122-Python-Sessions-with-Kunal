import re
string = "abhishek How are you"
regx = "^[a|A]"
if re.search(regx, string):
    print("Hey your String starts with A")
else:
    print("Better luck next time")
# Write A RE which matches the string only if it starts with [0-7] ends with @
# 3 mins 20:26

["9sdf@","fgdfg@","5asfsf#"]