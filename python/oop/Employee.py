# task 1
class Employee:
    def __init__(self,name,e_id,dep):
        self.name=name
        self.id=e_id
        self.dep=dep
        self.salary=30000
        self.type="Regular"
    def employeeDetails(self):
        print(f"Name:{self.name}, Dept {self.dep}\nEmployee id: {self.id}, Salary: {self.salary}")
        if self.type!="Regular":
            print(f"Employee Type:{self.type}")
    def workDistribution(self,dep):
        if dep!= "Human Resource":
            print("Collect work distribution loads from the HR department.")
        else:
            print("Collect work distribution details from the manager.")
    def increment(self):
        if self.type=="Regular":
            self.salary+=self.salary*(10/100)
            
        elif self.type=="Foreign":
            self.salary+=self.salary*(15/100)
        elif self.type=="Part Time":
            print("Sadly, there is no increment for the part time employees!!")
class Part_time_employee(Employee):
    def __init__(self,name,e_id,dep):
        super().__init__(name,e_id,dep)
        self.salary=15000
        self.type="Part Time"
        
class Foreign_employee(Employee):
    def __init__(self,name,e_id,dep):
        super().__init__(name,e_id,dep)
        self.type="Foreign"
    
    


print("1------------------------------------------")
emp1=Employee("Nawaz Ali", 102, "Marketing")
print("2------------------------------------------")
emp1.employeeDetails()
print("3------------------------------------------")
emp1.workDistribution("Marketing")
print("4------------------------------------------")
emp1.increment()
emp1.employeeDetails()
print("5------------------------------------------")
f_emp=Foreign_employee("Nadvi", 311, "Human Resource")
f_emp.employeeDetails()
print("6------------------------------------------")
f_emp.workDistribution("Human Resource")
print("7------------------------------------------")
f_emp.increment()
f_emp.employeeDetails()
print("8------------------------------------------")
p1_emp=Part_time_employee("Asif", 210, "Sales")
p2_emp=Part_time_employee("Olive", 223, "Accounts")
print("9------------------------------------------")
p1_emp.employeeDetails()
print("10------------------------------------------")
p1_emp.workDistribution("Sales")
print("11------------------------------------------")
p2_emp.increment()
print("12------------------------------------------")
p2_emp.employeeDetails()
