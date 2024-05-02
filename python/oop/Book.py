class book:
    def __init__(self, name):
        self.name = name
        self.genre='biography'
    def review(self):
         print('This book is just out of the world,mind-blowing!')

class fiction(book):
    def __init__(self,name,genre):
        super().__init__(name)
        book.genre=genre
    def review(self):
        print(f"{self.name} which is a {self.genre} is just out of the world, mind-blowing!")
class nonfiction(book):
    def __init__(self,name,):
        super().__init__(name)        
    def review(self):
        print(f"{self.name} which is a {self.genre} is just out of the world, mind-blowing!")
# Write your code here        

b1 = fiction('The Shining','Psychological horror')
b2 = nonfiction('A Beautiful Mind')
b1.review()
print('=========================')
b2.review()
print('=========================')




