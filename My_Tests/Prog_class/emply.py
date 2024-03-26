# this is class example of Class and inheritence
# Employees has few attributes which has been inherited to different classes down the line
# Manager, Developer, Tester are three classes where unique attributes are added to inherited attributes
# __str__ will display the employee details

class Employee:
    def __init__(self, name, age, num_year, salary):
        self.name = name
        self.age = age
        self.num_year = num_year
        self.salary = salary

    def __str__(self):
        return f"{self.name} {self.age} {self.num_year} {self.salary}"


class Manager(Employee):
    def __init__(self, name, age, num_year, salary, role):
        super().__init__(name, age, num_year, salary)
        self.role = role

    def manager_role(self):
        return f"Has manager role"


class Developer(Employee):
    def __init__(self, name, age, num_year, salary, prg_lang):
        super().__init__(name, age, num_year, salary)
        self.prg_lang = prg_lang

    def dev_role(self):
        return f"Developer writes code"


class QA(Employee):
    def __init__(self, name, age, num_year, salary, testing_tool):
        super().__init__(name, age, num_year, salary)
        self.testing_tool = testing_tool

    def qa_role(self):
        return f"Tester tests code"


m1 = Manager('PYB', 32, 8, 1000, 'manager')
print(m1.manager_role())
print(m1.role)
print(str(m1))

d1 = Developer('trassss', 44, 10, 2000, 'C+')
print(d1.dev_role())
print(d1.prg_lang)
print(str(d1))

t1 = QA('reytaysdt',25,2,500,'TH')
print(t1.qa_role())
print(t1.testing_tool)
print(str(t1))
