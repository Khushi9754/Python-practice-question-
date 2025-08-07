class Employee:
    def __init__(self,ID,name,salary):
        self.__id=ID
        self.__name=name
        self.__salary=salary

    def calculate_salary(self):
        print("The salary is",self.__salary)

    def get_salary(self):
        return self.__salary

    def set_salary(self,value):
        self.__salary=value
        

class Manager(Employee):
    def __init__(self,ID,name,salary,bonus,team_size,travel_allowance):
        super().__init__(ID,name,salary)
        self.bonus=bonus
        self.team_size=team_size
        self.travel_allowance=travel_allowance

    def calculate_salary(self):
        current_salary=self.get_salary()
        new_salary=current_salary+self.bonus
        print("managers salary",new_salary)
        super().calculate_salary()
        

class Developer(Employee):
    def __init__(self,ID,name,salary,overtime,payment_per_project):
        super().__init__(ID,name,salary)
        self.overtime=overtime
        self.payment_per_project=payment_per_project

    def calculate_salary(self):
        total_bonus=self.overtime*self.payment_per_project
        current_salary=self.get_salary()
        new_salary=current_salary+total_bonus
        print("developer salary",new_salary)


obj=Manager(1, "Khushi", 30000, 2000, 5, 8000)
obj1=Developer(2, "Ansh", 40000, 2, 5000)
obj.calculate_salary()
obj1.calculate_salary()