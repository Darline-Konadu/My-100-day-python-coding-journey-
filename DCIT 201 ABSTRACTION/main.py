from abc import ABC, abstractmethod


# Abstract Class
class Employee(ABC):
    def __init__(self, name: str, employee_id: str):
        self._name = name
        self._employee_id = employee_id

    def get_name(self):
        return self._name

    def get_employee_id(self):
        return self._employee_id

    @abstractmethod
    def calculate_pay(self):
        pass


# Derived Class
class FullTimeEmployee(Employee):
    def __init__(self, name: str, employee_id: str, salary: float):
        super().__init__(name, employee_id)
        self._salary = salary

    def get_salary(self):
        return self._salary

    def calculate_pay(self):
        return f"FullTimeEmployee Pay: {self._salary}"


# Instantiating FullTimeEmployee Object
employee = FullTimeEmployee("Darline Amoafo", "0243691528", 8000.0)

# Display Employee Details
print("Employee Name:", employee.get_name())
print("Employee ID:", employee.get_employee_id())
print("Salary:", employee.get_salary())
print("Pay Calculation:", employee.calculate_pay())
