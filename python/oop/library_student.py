class Library:
    Total_book = 1000
    borrow_data = {}
    
    def __init__(self,n,id):
        self.student_name = n
        self.student_id = id     
    
    def borrowbook(self):
        print("A book is borrowed!")
        
    def __str__(self):
        return "Library: XYZ"

#Write your code here  
class Student(Library):
    def __init__(self,name,id):
        super().__init__(name,id)
        self.book
    def borrowbook(self,name,id):
        
s1 = Student("Alice",18101259)
s1.borrowbook("The Alchemist", "Hdw652")
print("===============")
print(s1)
print("===============")
print(Library.borrow_data)
print("===============")
s1.borrowbook("Wuthering Heights")
print("===============")
print(s1)
print("===============")
s2= Student("David",18141777)
s2.borrowbook("The Alchemist", "Hdw652")
print("===============")
s2.borrowbook("The Vampyre")
print("===============")
print(Library.borrow_data)
print("===============")
s1.returnAllBooks()
print("===============")
print(Library.borrow_data)
