class Employee:
    # First we initialize the variables

    worked_hours = None
    rate = None
    tax_percentage = None
    gross_salary = None
    tax = None
    net_salary = None

    # Then we define a constructor method to create a new employee object
    
    def __init__(self, worked_hours: float, rate: float, tax_percentage: float):
        self.worked_hours = worked_hours
        self.rate = rate
        self.tax_percentage = tax_percentage

    # Now a method to compute the salary info

    def compute_salary_info(self) -> object:
        self.__compute_gross_salary()
        self.__compute_tax()
        self.__compute_net_salary()
        return self
    
    # Now we define private methods to compute the gross salary, the taxes, and the net salary
    
    def __compute_gross_salary(self) -> None:
        self.gross_salary = self.worked_hours * self.rate

    def __compute_tax(self) -> None:
        self.tax = self.gross_salary * self.tax_percentage / 100

    def __compute_net_salary(self) -> None:
        self.net_salary = self.gross_salary - self.tax

    # Finally, we define a function for printing the salary info

    def print_salary_info(self) -> None:
        print(f"EL SALARIO BRUTO ES: ${self.gross_salary:.2f}, LA RETENCIÓN EN LA FUENTE ES: ${self.tax:.2f}, EL SALARIO NETO ES: ${self.net_salary:.2f}")


# To test the code, do

if __name__ == '__main__':
    Employee(48, 5000, 12.5).compute_salary_info().print_salary_info()