# task 6
class Library:
    def __init__(self,name,books):
        self.name=name
        self.book_dict=books
        self.book_borrow={}
    def details(self):
        print(f"{self.name} Library details")
        print(f"Borrower details: \n {self.book_borrow}")
        print(f"Books availability:\n {self.book_dict}")  
class Reader:
    def __init__(self,name):
        self.name=name
        self.borrowed_books={}
        self.books=0
    def borrow(self,lib,*books):
        for book in books:
            if self.books<5:
                if book in self.borrowed_books:
                    self.borrowed_books[book]=1
                else:
                    self.borrowed_books[book]=0
                if lib.book_dict[book]==0:
                    print(f"{book} books are not available at the moment.")
                else:
                    self.borrowed_books[book]+=1
                    lib.book_dict[book]-=1
                    self.books+=1
                    
                    print(f"{book} books is borrowed successfully.")
            else:
                self.books=5
                print("You cannot borrow more than 5 books.")
            lib.book_borrow[self.name]=self.books
    def readerInfo(self,name=None):
            if name:
               print(f"{self.name}, you have {self.borrowed_books[name]} {name} book(s) with you.")
            else:
                print(f"{self.name}, you have {self.books} book(s) with you.")
                for book,count in self.borrowed_books.items():
                    if count!=0:
                        print(f"books on {book}:{count}")

# Driver Code
L1=Library('Dhaka',{'Arts':15,'Fiction':135,'Politics':2,'Science':11,'Poetry':15})
L1.details()
print("1----------------------")
r1=Reader('Aladdin')
r1.borrow(L1,'Arts','Fiction','Fiction','Politics')
print("2----------------------")
r1.borrow(L1,'Politics','Fiction')
print("3----------------------")
r1.readerInfo()
print("4----------------------")
r1.readerInfo('Fiction')
print("5----------------------")
L1.details()
print("6----------------------")
r2=Reader('Jasmine')
r2.borrow(L1,'Politics','Poetry')
print("7----------------------")
r2.readerInfo()
print("8----------------------")
L1.details()

