# 笨方法4



## 1.codeacademy 练习


   1）However, it's overwhelmingly common to use self as the first parameter in __init__()；
   
   2）Python will use the first parameter that __init__() receives to refer to the object being created;
   
   3）```class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00
        
class PartTimeEmployee(Employee):
    def calculate_wage(self,hours):
        self.hours = hours
        return hours* 12.00
        
    def full_time_wage(self,hours):
        self.hours = hours
        return super(PartTimeEmployee,self).calculate_wage(hours)
        
        
milton = PartTimeEmployee("James")
print milton.full_time_wage(20)```