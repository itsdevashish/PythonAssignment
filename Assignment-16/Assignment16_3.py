f = open("demo.txt", "r")
data = f.read()
f.close()

lines = data.split("\n")
words = data.split()
chars = list(data)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", len(chars))
