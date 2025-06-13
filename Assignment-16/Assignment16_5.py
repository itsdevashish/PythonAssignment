f = open("sample.txt", "r")
for line in f:
    if len(line.split()) > 5:
        print(line.strip())  # removes extra newline at the end
f.close()
