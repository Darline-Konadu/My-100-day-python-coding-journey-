class CommissionEmployee:
    def __init__(self, first_name: str, last_name: str, social_security_number: str, gross_sales: float, commission_rate: float):
        self._first_name = first_name
        self._last_name = last_name
        self._social_security_number = social_security_number
        self.set_gross_sales(gross_sales)  # Use setter to validate
        self.set_commission_rate(commission_rate)  # Use setter to validate

    # Getter and Setter for first_name
    def get_first_name(self) -> str:
        return self._first_name

    def set_first_name(self, first_name: str):
        self._first_name = first_name

    # Getter and Setter for last_name
    def get_last_name(self) -> str:
        return self._last_name

    def set_last_name(self, last_name: str):
        self._last_name = last_name

    # Getter and Setter for social_security_number
    def get_social_security_number(self) -> str:
        return self._social_security_number

    def set_social_security_number(self, social_security_number: str):
        self._social_security_number = social_security_number

    # Getter and Setter for gross_sales
    def get_gross_sales(self) -> float:
        return self._gross_sales

    def set_gross_sales(self, gross_sales: float):
        if gross_sales < 0.0:
            raise ValueError("Gross sales must be ≥ 0.0")
        self._gross_sales = gross_sales

    # Getter and Setter for commission_rate
    def get_commission_rate(self) -> float:
        return self._commission_rate

    def set_commission_rate(self, commission_rate: float):
        if not (0.0 <= commission_rate <= 1.0):
            raise ValueError("Commission rate must be between 0.0 and 1.0")
        self._commission_rate = commission_rate

    # Method to calculate earnings
    def earnings(self) -> float:
        return self._gross_sales * self._commission_rate

    # Method to display employee details
    def display_employee_details(self):
        print(f"Employee Details:")
        print(f"First Name: {self._first_name}")
        print(f"Last Name: {self._last_name}")
        print(f"Social Security Number: {self._social_security_number}")
        print(f"Gross Sales: {self._gross_sales}")
        print(f"Commission Rate: {self._commission_rate}")
        print(f"Earnings: ${self.earnings():.2f}")


class BasePlusCommissionEmployee(CommissionEmployee):
    def __init__(self, first_name: str, last_name: str, social_security_number: str, gross_sales: float, commission_rate: float, base_salary: float):
        super().__init__(first_name, last_name, social_security_number, gross_sales, commission_rate)
        self.set_base_salary(base_salary)  # Use setter to validate

    # Getter and Setter for base_salary
    def get_base_salary(self) -> float:
        return self._base_salary

    def set_base_salary(self, base_salary: float):
        if base_salary < 0.0:
            raise ValueError("Base salary must be ≥ 0.0")
        self._base_salary = base_salary

    # Override earnings method to include base salary
    def earnings(self) -> float:
        return self._base_salary + (self._gross_sales * self._commission_rate)

    # Override display_employee_details to include base salary
    def display_employee_details(self):
        super().display_employee_details()
        print(f"Base Salary: ${self._base_salary:.2f}")
        print(f"Total Earnings (including base salary): ${self.earnings():.2f}")


# An instance of Commission-Only Employees
commission_employee = CommissionEmployee(
    first_name="Alice",
    last_name="Smith",
    social_security_number="987-65-4321",
    gross_sales=50000.0,
    commission_rate=0.1
)

# An instance of BasePlusCommission Employees
base_plus_commission_employee = BasePlusCommissionEmployee(
    first_name="Darline",
    last_name="Amoafo",
    social_security_number="456-78-9123",
    gross_sales=60000.0,
    commission_rate=0.15,
    base_salary=2000.0
)

#  Calculate and Display Earnings for each employee
print("Commission-Only Employee:")
commission_employee.display_employee_details()

print("\nBase Plus Commission Employee:")
base_plus_commission_employee.display_employee_details()

# Update baseSalary for a BasePlusCommissionEmployee instance and print the updated earnings
base_plus_commission_employee.set_base_salary(3000.0)
print("\nAfter updating base salary:")
base_plus_commission_employee.display_employee_details()