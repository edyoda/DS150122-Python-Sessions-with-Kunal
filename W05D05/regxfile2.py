import re

regx = "^[0-7].*@"
list_of_strings = ["7sdf@","fgdfg@","55asfsf@#","6@"]

for i in list_of_strings:
    # print(regx == i)
    if re.search(regx, i):
        print(i)
    else:
        print(f"{i} is not a match")