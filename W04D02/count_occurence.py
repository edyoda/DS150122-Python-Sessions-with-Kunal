# Q3) you are given a string count the number of occurence of each letters:
#     asdddfgtttgfsssdeewwqqaswfd
s  =input("Enter the string: ")
dict1 = {}
for i in s:
    if i not in dict1.keys():
        dict1[i] = 1
    else:
        dict1[i]+=1
print(dict1)