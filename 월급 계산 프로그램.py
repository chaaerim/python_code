class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.salary

    def __str__(self):
        return f'이름: {self.name}, 월급: {self.getSalary()}'


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def getSalary(self):
        return super().getSalary() + self.bonus


kim = Employee('김길동', 10000)
lee = Manager('이수만', 200000, 300000)
lee.getSalary()
print(kim)
print(lee)
