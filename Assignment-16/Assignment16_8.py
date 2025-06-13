f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
for line in f1:
    if line.strip() != "":
        f2.write(line)
f1.close()
f2.close()