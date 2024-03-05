# Task 5
class Author:
    def __init__(self,name=None):
        if name==None:
            print("A book can not be added without author name")
            self.name=""
        else:
            self.name=name
        self.num=0
        self.data1={}
    def setName(self,name):
        if self.name=="":
            self.name=name
    def addBook(self,book_name,genre):
        if book_name not in self.data1.values():
            if genre in self.data1:
                self.data1[genre]+=", "+book_name
                self.num+=1
            else:
                self.data1[genre]=book_name
                self.num+=1
    def printDetail(self):
        print(f"Number of Book(s): {self.num}")
        print(f"Author Name: {self.name}")
        for k ,l in self.data1.items():
            print(f"{k}:{l}")
    
# Write your code here 
# Do not change the following lines of code. 
a1 = Author() 
print("=================================")
a1.addBook("Ice", "Science Fiction") 
print("=================================") 
a1.setName("Anna Kavan") 
a1.addBook("Ice", "Science Fiction") 
a1.printDetail() 
print("=================================") 
a2 = Author("Humayun Ahmed") 
a2.addBook("Onnobhubon", "Science Fiction") 
a2.addBook("Megher Upor Bari", "Horror") 
print("=================================") 
a2.printDetail() 
a2.addBook("Ireena", "Science Fiction") 
print("=================================") 
a2.printDetail() 
print("=================================")
