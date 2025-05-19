class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name # public variable
        self._salary = salary # protected variable
        self.__ssn = ssn # private variable

        
if __name__ == "__main__":
    emp = Employee("Iraj", 60000, "12345678901") 
    print(emp.name)
    print(emp._salary)
    try:
        print(emp.__ssn)
    except AttributeError:
        print("Cannot access private variable __ssn.")    
            