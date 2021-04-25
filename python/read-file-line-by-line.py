filename = "test-text-file.txt"
with open(filename, "r") as fs:
    for line in fs:
        line = line.rstrip("\n")
        print(line.replace("\n", "\\n"))
