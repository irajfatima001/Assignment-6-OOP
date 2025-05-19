class Employee :
    def __init__(self, name):
        self.name =  name



class Department:  
    def __init__(self, employee):
        self.employee = employee


emp1 = Employee("Iraj")

dept1 = Department(emp1)
print("Employee in department:", dept1.employee.name)