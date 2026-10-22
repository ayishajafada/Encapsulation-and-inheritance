#Create a Student class with private attribute __marks. Create methods to set and display marks. Allow marks only between 0 and 100.

class student:
    def __init__(self,__marks):
        self.__marks=__marks
    def display_marks(self):
        return self.__marks
        print(self.__marks)
    def set_marks(self,marks):
        if 0<marks<100:
            self.__marks=marks
            print("marks updated uccessfully")
        else:
            print("Invalid marks")

student1=student(86)
student1.display_marks()   
print(student1.display_marks())

#2Create a BankAccount class with private __balance. Create deposit(), withdraw(), and check_balance() methods.

class bank_account:
    def __init__(self,balance):
        self.__balance=balance
    def deposite(self,amount):
        if amount>0:
            self.__balance+=amount
            print("amount deposited successfully")
        else:
            print("Enter a valid amount")

    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
            print("amount withdrawn successfully")
        else:
            print("Insufficient balance")
    def check_balance(self):
        print("current balance:", self.__balance)

bank_account1=bank_account(38000)
bank_account1.deposite(5000)
bank_account1.check_balance()
bank_account1.withdraw(9000)
bank_account1.check_balance()

#3Create a Mobile class with private __battery. Create methods charge() and check_battery(). Battery should never exceed 100%.

class mobile:
    def __init__(self):
        self.__battery=0
    def charge(self,percentage):
        self.__battery+=percentage
        if self.__battery>100:
            self.__battery=100
            
    def check_battery(self,):
        print("Battery:",self.__battery,"%")

phone=mobile()
phone.charge(30)
phone.check_battery()
phone.charge(90)
phone.check_battery()

##4  Create an Employee class with private __salary. Create a method to increase salary only when the given amount is positive.

class employee:
    def __init__(self,__salary):
        self.__salary=__salary
    def increased_salary(self,amount):
        if amount>0:
            self.__salary+=amount
        else:
            print("invalid amount")

    def get_salary(self):
        return self.__salary
    
emp1=employee(38000)

print("Initial salary :",emp1.get_salary())

emp1.increased_salary(5000)
print("Increased salary :",emp1.get_salary())

##5 Create a Car class with private __speed. Create accelerate() and brake() methods. Speed should never become negative.

class car:
    def __init__(self,__speed):
        self.__speed=__speed

    def accelerate(self,amount):
        if amount>0:
            self.__speed+=amount
        else:
            print("Invalid CCELERATION AMOUNT!")

    def brake(self,amount):
        if amount>0:
            self.__speed-=amount
            if self.__speed<0:
                self.__speed=0
        else:
            print("Invalid Brake amount!")

    def check_speed(self):
        print("current speed : ",self.__speed ,"km/hr")

car1 = car(60)

car1.check_speed()       
car1.accelerate(50)
car1.check_speed()      
car1.brake(20)
car1.check_speed()     
car1.brake(50)
car1.check_speed()       

##6 Create a Temperature class with private __temperature. Create a method to set the temperature. Don't allow temperature below -273.15°C.

class Temperature:
    def __init__(self,__temperature):
        self.__temperature=__temperature

    def set_temperature(self,new_temp):
        if new_temp>-273.15:
            self.__temperature=new_temp
        else:
            print("Temperature cannot go below -273.15!")

    def get_temperature(self):
        return self.__temperature

temp1=Temperature(25)
temp1.set_temperature(25)
print("Temperature:",temp1.get_temperature())

temp1.set_temperature(-300)
print("Temperature:",temp1.get_temperature())





######Inheritance

#1 Create a parent class Animal with a method eat(). Create a child class Dog with a method bark(). Create a Dog object and call both methods.

class animal:
    def eat(self):
        print("animal is eating")
class dog(animal):
    def bark(self):
        print("Dog is barking")

dog1=dog()
dog1.eat()
dog1.bark()

##2 Vehicle and Car Create a parent class Vehicle with a method: start() Create a child class Car with a method: drive() Create a Car object and call both methods.

class vehicle:
    def start(self):
        print("vehicle is starting")
    

class car(vehicle):
    def drive(self):
        print("car is driving")

car1=car()
car1.start()
car1.drive()

##3 Person and Student Create a parent class Person with attributes: •  name •  age Create a child class Student with an additional attribute: •  course Display all three details

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_perosn_details(self):
        print("name:",self.name , "age:",self.age)
class student(person):
    def __init__(self,name,age,course):
        self.course=course
        super().__init__(name,age)
        
    def display_student(self):
        self.display_perosn_details()
        print("course:",self.course)

student1=student("ayisha",27,"Machine learning")
student1.display_student()

##4 Employee and Developer Create a parent class Employee with: name salary display_details() Create a child class Developer with: write_code() Create an object and call all methods.

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_details(self):
        print("name:",self.name)
        print("salary:",self.salary)
class developer(employee):
    def write_code(self):
        print("Developer writes code")


employee1=developer("ayisha",30000)
employee1.display_details()
employee1.write_code()

##5  Shape and Rectangle Create a parent class Shape with a method: display() Create a child class Rectangle with: •  length •  breadth •  calculate_area() Calculate and display the area.

class shape:
    def display(self):
        print("This is a shape")

class rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def calculate_area(self):
        return self.length*self.breadth
    def display(self):
        print("Length:", self.length)
        print("Breadth:", self.breadth)
        print("Area:", self.calculate_area())

shape1=rectangle(7,9)
shape1.display()

##6 Animal and Cat Create a parent class Animal with: eat() sleep() Create a child class Cat with: meow() Create a Cat object and call all three methods.

class animal:
    def eat(self):
        print("animal is eating")
    def sleep(self):
        print("animal is sleeping")

class cat(animal):
    def meow(self):
        print("cat sound meow")

anim1=cat()
anim1.eat()
anim1.sleep()
anim1.meow()

##7 Bank Account and Savings Account Create a parent class BankAccount with: deposit() withdraw() Create a child class SavingsAccount with: add_interest() Create an object and test all three methods.

class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("amount deposited :",amount)
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("amount withdrawn:",amount)
        else:
            print("insufficient balance")


class SavingsAccount(BankAccount):
    def add_interest(self,rate=7):
        self.rate=rate
        interest=self.balance*rate/100
        self.balance+=interest
        print("interest added:",interest)


acc1=SavingsAccount(27000)
acc1.deposit(6000)
acc1.withdraw(5000)
acc1.add_interest()

###8 Person and Teacher Create a parent class Person with: name age display_person() Create a child class Teacher with: subject display_subject() Display all the details.

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person(self):
        print("name:",self.name)
        print("age:",self.age)

class teacher(person):
        def display_subject(self,subject):
            self.subject=subject

            print("subject:",self.subject)
       


teachr=teacher("ayisha",27)
teachr.display_person()
teachr.display_subject("mathematics")

###9 Create a parent class Vehicle with: def start(self): print("Vehicle is starting") Create a child class Bike and override the start() method: Bike is starting with a kick Create a Bike object and call start().

class vehicle:
    def start(self):
        print("vehicle is starting")

class bike(vehicle):
    def start(self):
        print("bike is starting with a kick")

bike1=bike()
bike1.start()

###9  Person → Student → CollegeStudent Create three classes: Person ↓ Student ↓ CollegeStudent Person — Store: •  name •  age Student — Add: •  roll_number CollegeStudent — Add: •  college_name Create a CollegeStudent object and display all four details.

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person(self):
        print("Name:",self.name)
        print("Age:",self.age)
class student(person):
    def __init__(self,name,age,roll_number):
        super().__init__(name,age)
        self.roll_number=roll_number

    def display_student(self):
        print("roll_number:",self.roll_number)


class college_student(student):
    def __init__(self,name,age,roll_number,college_name):
        super().__init__(name,age,roll_number)

        self.college_name=college_name
    def display_college_student(self):

        print("name of college:",self.college_name)

college_student1=college_student("ayisha",27,10,"BIT")
college_student1.display_person()
college_student1.display_student()
college_student1.display_college_student()
