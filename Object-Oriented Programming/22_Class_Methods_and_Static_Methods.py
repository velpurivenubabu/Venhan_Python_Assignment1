class Employee:
    num_employees = 0
    
    def __init__(self, employee_id: str):
        self.employee_id = employee_id
        Employee.num_employees += 1
    

    @classmethod
    def get_num_employees(cls) -> int:
        return cls.num_employees
    

    @staticmethod
    def validate_employee_id(employee_id: str) -> bool:
        return employee_id.isdigit()  # Check if the ID consists only of digits

# Example :
employee1 = Employee("452545")
employee2 = Employee("61587890")

print("Number of Employees:", Employee.get_num_employees())

employee3 = Employee("ABCDE")

print("Is 'ABCDE' a valid employee ID?", Employee.validate_employee_id("SWWRTE"))
print("Is '12345' a valid employee ID?", Employee.validate_employee_id("452545"))
