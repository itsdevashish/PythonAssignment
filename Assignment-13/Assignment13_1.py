class bookstore():

    noofbooks=0

    def __init__(self,name,author):
        self.name=name
        self.author=author
        bookstore.noofbooks +=1
    
    def display(self):
        print(self.name,self.author,bookstore.noofbooks)
    

obj1=bookstore("Linux System Programming", "Robert Love")
obj1.display()

obj1=bookstore("C Programming", "Dennis Ritchie")
obj1.display()





