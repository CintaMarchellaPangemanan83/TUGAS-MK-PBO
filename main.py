class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Company:
    def __init__(self, name):
        self.name = name
        self.__employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.__employees.append(employee)
            print("Employee berhasil ditambahkan.")
        else:
            print("Object bukan Employee.")

    def __calculate_payroll(self):
        total = 0

        for employee in self.__employees:
            total += employee.salary

        return total

    def show_company(self):
        print("Nama Company:", self.name)
        print("Jumlah Employee:", len(self.__employees))
        print("Total Payroll:", self.__calculate_payroll())


company = Company("PT Teknologi Indonesia")

employee1 = Employee("Cinta", 5000000)
employee2 = Employee("Jesicca", 4500000)
employee3 = Employee("Shiren", 7000000)

company.add_employee(employee1)
company.add_employee(employee2)
company.add_employee(employee3)

company.show_company()
