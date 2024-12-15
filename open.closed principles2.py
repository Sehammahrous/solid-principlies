class Employee:
    def calculate_salary(self,hours_work):
        raise NotImplementedError("This method should be overridden by subclasses.")
    
class FullTimeEmployee(Employee):
    def calculate_salary(self,hours_work):
        return hours_work*100

class PartTimeEmployee(Employee):
    def calculate_salary(self,hours_work):
        return hours_work*50
    
class InternalEmployee(Employee):
    def calculate_salary(self,hours_work):
        return hours_work*25
    
    
fulltimeemoloyee=FullTimeEmployee()
parttimeemployee=PartTimeEmployee()
internalemployee=InternalEmployee()

print("calculate_salary of FullTimeEmployee:", fulltimeemoloyee.calculate_salary(24)) 
print("calculate_salary of PartTimeEmployee:", parttimeemployee.calculate_salary(15))  
print("Salary of InternalEmployee:", internalemployee.calculate_salary(10) ) 
    

