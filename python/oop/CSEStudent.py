class Student:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
    def Details(self):
        return "Name: "+self.name+"\n"+"ID: "+self.ID+"\n"
#Write your code here
class CSEStudent(Student):
    def __init__(self,name,id,sem):
        super().__init__(name,id)
        self.sem=sem
        self.cgpa={}
    def Details(self):
        return f"Name: {self.name}\nID: {self.id}\nCurrent semester: {self.sem}"

    def addCourseWithMarks(self,*cor_mark):
        for name,mark in cor_mark:
            grade=0
            if mark>=85:
                grade=4.0
            elif 80<=mark<=84:
                grade=3.3
            elif 70<=mark<=79:
                grade=3.0
            elif 65<=mark<=69:
                grade=2.3
            elif 57<=mark<=64:
                grade=2.0
            elif 80<=mark<=84:
                grade=3.3
        
        
        
Bob = CSEStudent("Bob","20301018","Fall 2020")
Carol = CSEStudent("Carol","16301814","Fall 2020")
Anny = CSEStudent("Anny","18201234","Fall 2020")
print("#########################")
print(Bob.Details())
print("#########################")
print(Carol.Details())
print("#########################")
print(Anny.Details())
print("#########################")
Bob.addCourseWithMarks("CSE111",83.5,"CSE230",73.0,"CSE260",92.5)
Carol.addCourseWithMarks("CSE470",62.5,"CSE422",69.0,"CSE460",76.5,"CSE461",87.0)
Anny.addCourseWithMarks("CSE340",45.5,"CSE321",95.0,"CSE370",91.0)
print("----------------------------")
Bob.showGPA()
print("----------------------------")
Carol.showGPA()
print("----------------------------")
Anny.showGPA()
