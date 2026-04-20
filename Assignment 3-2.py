class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        self.hra = 0.20 * self.basic_salary
        self.da = 0.10 * self.basic_salary
        self.tax = 0.05 * self.basic_salary
        self.pf = 0.12 * self.basic_salary

        self.gross_salary = self.basic_salary + self.hra + self.da
        self.total_deductions = self.tax + self.pf
        self.net_salary = self.gross_salary - self.total_deductions

    def display_salary(self):
        print("\n-Salary Slip ")
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", self.hra)
        print("DA:", self.da)
        print("Gross Salary:", self.gross_salary)
        print("Tax:", self.tax)
        print("PF:", self.pf)
        print("Total Deductions:", self.total_deductions)
        print("Net Salary:", self.net_salary)

emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

emp = Employee(emp_id, name, basic_salary)
emp.calculate_salary()
emp.display_salary()
