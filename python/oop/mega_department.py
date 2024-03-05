# Task 3
class Department:
    def __init__(self,name="ChE Department",section=5):
        self.name=name
        self.section=section
        self.students=[]
        print(f"The {self.name} has {self.section} sections.")
    def avg_students(self):
        if self.students:
            return sum(self.students)/len(self.students)
        else:
            return 0
        
    def add_students(self,*num):
        if len(num)==self.section:
            self.students=list(num)
            print(f"The {self.name} has an average of {self.avg_students():.2f} students in each section.")
        else:
            print(f"The {self.name} Department doesn't have {self.section} sections.")
    
    
    def merge_Department(self,*args):
        merged_students = self.students
        sum1=0
        for i in args:
            merged_students+=i.students
            merged_dpt=i.name
            print(f"{merged_dpt} is merged to {self.name}.")
        for i in merged_students:
            sum1+=i
        return f"Now the {self.name} has an average of {sum1/self.section} students in each section."



# Driver Code
d1 = Department()
print('1-----------------------------')
d2 = Department('MME Department')
print('2-----------------------------')
d3 = Department('NCE Department', 8)
print('3-----------------------------')
d1.add_students(12, 23, 12, 34, 21)
print('4-----------------------------')
d2.add_students(40, 30, 21)
print('5-----------------------------')
d3.add_students(12, 34, 41, 17, 30, 22, 32, 51)
print('6-----------------------------')
mega = Department('Engineering Department', 10)
print('7-----------------------------')
mega.add_students(21,30,40,36,10,32,27,51,45,15)
print('8-----------------------------')
print(mega.merge_Department(d1, d2))
print('9-----------------------------')
print(mega.merge_Department(d3))



