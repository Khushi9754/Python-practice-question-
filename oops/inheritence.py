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


#hierarchical inhe...**********************************************************************************************
class Vehicle:
    def __init__(self,vehicle_no,model,brand):
        self.__vehicle_no=vehicle_no
        self.__model=model
        self.__brand=brand
        
    def fuel_type(self):
        print("this vehicle uses fuel")

class Car(Vehicle):
    def __init__(self,vehicle_no,brand,boot_space,sunroof):
        super().__init__(vehicle_no,None,brand)
        self.boot_space=boot_space
        self.sunroof=sunroof

    def fuel_type(self):
        print("car uses Petrol or Diesel")
        super().fuel_type()
        
    
class Bike(Vehicle):
    def __init__(self,vehicle_no,brand,engine_cc,car_type):
        super().__init__(vehicle_no,None,brand)
        self.engine_cc=engine_cc
        self.car_type=car_type

    def fuel_type(self):
        print("Bike uses petrol")
    
class Bus(Vehicle):
    def __init__(self,vehicle_no,brand,seating_capacity,bustype):
        super().__init__(vehicle_no,None,brand)
        self.seating_capacity=seating_capacity
        self.bustype=bustype

    def fuel_type(self):
        print("bus uses diesel or CNG")

c1 = Car("MP09AB1234", "Hyundai", "450L", True)
c1.fuel_type()

b1 = Bike("MP09XY6789", "Yamaha", "150cc", "Sports")
b1.fuel_type()

bu1 = Bus("MP09PK2345", "Volvo", 45, "AC Sleeper")
bu1.fuel_type()
