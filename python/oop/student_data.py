# Task 4
class StudentDatabase:
    def __init__(self,name,stu_id):
        self.name=name
        self.grades={}
        self.id=stu_id
        
    def calculateGPA(self, courses, semester):
        total_gpas = 0
        credit_p = 0
        for course in courses:
            course_name, gpa = course.split(':')
            total_gpas += float(gpa)
            credit_p += 1
        if semester not in self.grades:
            self.grades[semester] = {}
        self.grades[semester][tuple(courses)] = round(total_gpas / credit_p, 2)
    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        for sem, course in self.grades.items():
            print(f"Courses taken in {sem}:")
            for names, cgpa in course.items():
                for k in names:
                    for l in k.split(":"):
                        if not ("0">=l[0]<="9"):
                            print(l)
            
                    
            print(f"CGPA: {cgpa}")
            print()        
                
        
        


# Write your code here
s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('---------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
print('---------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('---------------------------------')
s2.printDetails()
