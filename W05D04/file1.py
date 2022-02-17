with open("name.txt", "r+") as fp:
    fp.write("Hey Snegha Did you complete your Assignment?")
    fp.seek(0)
    print(fp.read())