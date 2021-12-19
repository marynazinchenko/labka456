# поля
# прізвище та ініціали;
# дата народження (член-клас);
# дата прийняття на роботу (член-клас);
# розмір заробітної плати;
# методи
# визначення стажу роботи працівника;
# визначення віку працівника на даний момент;
# визначення загальної виплаченої суми коштів протягом всього періоду роботи.

from datetime import datetime

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y/%m/%d")
    d2 = datetime.strptime(d2, "%Y/%m/%d")
    return abs((d2 - d1).days)
def month_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y/%m/%d")
    d2 = datetime.strptime(d2, "%Y/%m/%d")
    return (d2.year - d1.year) * 12 + (d2.month - d1.month) - 1
def years_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y/%m/%d")
    d2 = datetime.strptime(d2, "%Y/%m/%d")
    return d2.year - d1.year

class Employee:
    def __init__(self, name, age, salary, work):
        self.name = name
        self.age = age
        self.salary = salary
        self.work = work
    def get_work(self):
        now = datetime.now()  # current date and time
        print(days_between(self.work, now.strftime("%Y/%m/%d")))
    def get_whole_salary(self):
        now = datetime.now()  # current date and time
        print(month_between(self.work, now.strftime("%Y/%m/%d")) * self.salary)
    def get_age(self):
        now = datetime.now()  # current date and time
        print(years_between(self.age, now.strftime("%Y/%m/%d")))

employee_birthday = "2000/12/12"
employee_startwork = "2018/10/27"
input_data = Employee("Ivan", employee_birthday, 1500, employee_startwork)
input_data.get_work()
input_data.get_whole_salary()
input_data.get_age()

