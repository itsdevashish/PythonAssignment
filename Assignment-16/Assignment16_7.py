fobj = open("marks.txt", "w")
for i in range(5):
    name = input("Name: ")
    marks = input("Marks: ")
    fobj.write(name + " " + marks + "\n")
fobj.close()

f = open("marks.txt", "r")
for line in f:
    name, marks = line.split()
    if int(marks) > 75:
        print(name, marks)
f.close()
