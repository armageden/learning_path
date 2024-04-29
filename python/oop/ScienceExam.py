# task 2
class Exam:
    def __init__(self,marks):
        self.marks = marks
        self.time = 60
        
    def examSyllabus(self):
        return "Maths , English"
    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"
#    write from here

class ScienceExam(Exam):
    def __init__(self,mark,time,*sub):
        super().__init__(mark)
        self.time=time
        self.sub=[]
        self.part=2
        for i in sub:
            self.part+=1
            self.sub.append(i)
    def examSyllabus(self):
        list_sub=super().examSyllabus()
        for i in self.sub:
            list_sub+=" , "+i
        return list_sub
    def examParts(self):
        total=3
        string1=super().examParts()
        for i in self.sub:
            string1+=(f"Part {str(total)} - {i}\n")
            total+=1 
        return string1
    def __str__(self):
        return (f"Marks: {self.marks} Time: {self.time} minutes Number of Parts: {self.part}")    
    
engineering = ScienceExam(100,90,"Physics","HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================') 
architecture = ScienceExam(100,120,"Physics","HigherMaths","Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())