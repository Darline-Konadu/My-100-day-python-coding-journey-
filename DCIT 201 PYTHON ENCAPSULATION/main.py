class CommissionEmployee:
    def __init__(self, first_name: str, last_name: str, social_security_number: str, gross_sales: float, commission_rate: float):
        self._first_name = first_name
        self._last_name = last_name
        self._social_security_number = social_security_number
        self.set_gross_sales(gross_sales)
        self.set_commission_rate(commission_rate)

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
    def display_details(self):
        print(f"Employee Details:")
        print(f"First Name: {self._first_name}")
        print(f"Last Name: {self._last_name}")
        print(f"Social Security Number: {self._social_security_number}")
        print(f"Gross Sales: {self._gross_sales}")
        print(f"Commission Rate: {self._commission_rate}")
        print(f"Earnings: {self.earnings()}")


# Creating an instance of the CommissionEmployee class
employee = CommissionEmployee(
    first_name="Darline",
    last_name="Amoafo",
    social_security_number="024-36-91528",
    gross_sales=80000.0,
    commission_rate=0.2
)

# Updating the employee’s grossSales and commissionRate and  displaying the updated details
employee.set_gross_sales(70000.0)
employee.set_commission_rate(0.12)

# Display updated details
employee.display_details()

# Calculate and display the employee’s earnings using the earnings() method
print(f"Employee Earnings: ${employee.earnings():.2f}")