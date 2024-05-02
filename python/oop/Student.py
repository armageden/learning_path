class Student:
    all_count=0
    cse=0
    bba=0
    def __init__(self,name,dep):
        self.name=name
        self.dep=dep
        Student.all_count+=1
        self.serial_all=Student.all_count
        
        
        if dep=="BBA":
            Student.bba+=1
            self.serial_dep=Student.bba
        else:
            Student.cse+=1
            self.serial_dep=Student.cse
        
    def individualInfo(self):
        print(f"Naruto is from {self.dep} department.\nSerial of Naruto among all students' is: {self.serial_all}\nSerial of Naruto in {self.dep} department is: {self.serial_dep}")
    def totalInfo(self):
        print(f"Total Number of Student: {self.all_count}\nTotal Number of CSE Student: {self.cse}\nTotal Number of BBA Student: {self.bba}")   


# Write Your Code Here


s1 = Student("Naruto", "CSE")
print('----------------------')
s1.individualInfo()
print('#############################')
s1.totalInfo()
print('============================')


s2 = Student("Sakura", "BBA")
print('----------------------')
s2.individualInfo()
print('#############################')
s2.totalInfo()
print('============================')


s3 = Student("Shikamaru", "CSE")
print('----------------------')
s3.individualInfo()
print('#############################')
s3.totalInfo()
print('============================')


s4 = Student("Deidara", "BBA")
print('----------------------')
s4.individualInfo()
print('#############################')
s4.totalInfo()
