# class Node:
#     def __init__(self,item=None,Next=None):
#         self.item=item
#         self.Next=Next
        
# class SLL:
#     def __init__(self,start=None):
#         self.start=start
        
#     def is_empty(self):
#         return self.start==None
    
#     def insert_at_start(self,data):
#         n=Node(data,self.start)
#         self.start=n
    
#     def insert_at_last(self,data):
#         n=Node(data)
#         temp=self.start
#         if not self.is_empty():
#             while temp.Next is not None:
#                 temp=temp.Next
#             temp.Next=n
#         else:
#             self.start=n      


# Title='Saint Johns Hosptal'
# class Patiant():
#     def __init__(self,Name,age,sex,Zipcode):
#         self.Name=Name
#         self.age=age
#         self.sex=sex
#         self.Zipcode=Zipcode
#     def get_detail(self):
#         print(f"the patiant name is {self.Name} age is {self.age} gender is {self.sex} and the zipcode is {self.Zipcode}")
     
#     def __init__(self,surgery):
#          self.surgery=surgery
#          super().__init__()   
# p1=Patiant('rahul',30,'male',12345,'heart')
# p1.get_detail()
    

# Title='saint Johns Hospital'
# class Patient:
#     def __init__(self,Name,Age,Sex,Zipcode,state):
#         self.Name=Name
#         self.Age=Age
#         self.Sex=Sex
#         self.Zipcode=Zipcode
#         self.state=state
    
#     def get_detail(self):
#         if self.state=='ca':
#             self.state='canada'
#         elif self.state=='ind':
#             self.state='India'
#         elif self.state == 'us':
#             self.state='unite State'
#         elif self.state=='uk':
#             self.state='united kingdom'
#         elif self.state=='ch':
#             self.state='china'
#         print(f"The patient name is {self.Name} age is {self.Age} gender is {self.Sex} Zipcode is {self.Zipcode} and the state is {self.state}")
        
# p1=Patient('Rahul',32,'male',12342,'ind')
# p2=Patient('Nitin',42,'female',12321,'ch')
# p1.get_detail()
# p2.get_detail()




# create a calss with the name employee working in google and store the data like name address salary

# class Employee:
#     company="Google"
#     def __init__(self,name,salary,address):
#         self.name=name
#         self.salary=salary
#         self.address=address
        
#     def get_detail(self):
#         print(f"the employee name is {self.name} working in {Employee.company} salary is {self.salary} and address is {self.address} ")

# emp=Employee("Rahul",12000,"kandivali")
# emp1=Employee("Rajesh",19000,"poisar")
# emp.get_detail() 
# emp1.get_detail()




# class Employee:
#     conpany="ABC"
#     def m1(self):
#         self.name="rahul"
#         self.salary=12000
#         self.address="Kandivali"
    
#     def get_detail1(self):
#         print(f"the name of an employee {self.name} salary {self.salary} and adress {self.address}")
        
# e=Employee()
# e.m1()



 
# a=11
# b=2
# c=a//b
# n=a%b
# print(c)
# print(n)

# num=int(input("enter the number:"))
# num1=num//10
# num2=num%10
# print(num1)
# print(num2)



# instence variable

# class Student:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
        
# s1=Student("Anjli",101)
# s2=Student("Aman",104)
# print(f"the name of an Student is {s1.name} and {s1.id}")
# print(f"the name of an Student is {s2.name} and {s2.id}")


# where instance veriable can be declare

# 1. By using a constructor
# 2. By using a instance Method
# 3. by using a object name



# 1. By using a constructor

# class Employee:
#     def __init__(self,id,name,address):
#         self.id=id
#         self.name=name
#         self.address=address
        
# E1=Employee(101,"Anjali","Kandivali")
# E2=Employee(102,"Raja","Virar")

# print(f"the id of an Employee is {E1.id} name is {E1.name} and the address is {E1.address}")
# print(f"the id of an Employee is {E2.id} name is {E2.name} and the address is {E2.address}")
# print(E1.__dict__)
# print(E2.__dict__)

# **********************  2. By using a instance Method  ****************************

# class Employee:
#     def persion1(self):
#         self.id=101
#         self.name='Radha'
#         self.salary=12000
#         print(f"the id of an employee is {self.id} name is {self.name} and salary is {self.salary}")
        
# emp1=Employee()
# emp1.persion1()

# #*************************** 2nd ********************************

# class Student:
#     def persion(self):
#         self.id=102
#         self.name="Rahul"
#         self.address="kandivali"
#         print(f"the id is {self.id} name is {self.name} and address is {self.address}")

# S=Student()
# S.persion()

# #********************************** Declaring instance veriable using object name **************************8

# class Test:
#     def __init__(self):
#         print("this is constructor")
        
#     def m2(self):
#         print("This is instance method")
        
# t=Test()
# t.m2()
# t.a=10
# t.b=20
# t.c=30
# print(t.a,t.b,t.c)
# print(t.__dict__)

# class emp:
#     company="ABC"
#     def __init__(self):
#         pass
    
# r=emp()
# print(emp.company)
# print(r.company)


# class Demo:
#     def __init__(self):
#         Demo.a=100
# d=Demo()
# print(Demo.__dict__)

# class Demo1:
#     def em(self):
#         Demo1.b=200
#         print(f"the number id {Demo1.b}")
        
# d=Demo1()
# d.em()
# print(Demo1.__dict__)

# ************************************* Setter and Getter **************************************

class Coustomer:
    def persion_name(self,name):
        self.name=name
        
    def persion_salary(self,salary):
        self.salary=salary
        
v=Coustomer()
v.persion_name("DDDDDDD")
v.persion_salary(120000)
print(v.name)
print(v.salary)

#*************************************** 2nd *************************************************

class Coustomer1:
    def __init__(self,name,id):     
        self.name=name
        self.id=id
        
    def add_coutomer_detail(self,Store_name):   
        self.Store_name=Store_name
        
cou=Coustomer1("Vinod",101)
cou.add_coutomer_detail("Vinod_general_Store")

print(f"the Onwer name is {cou.name} id is {cou.id} and Store name is {cou.Store_name}")

# ********************************** Getter ***********************************************

class coustomer2:
    def __init__(self,name):
        self.name=name
        
    def getter_data(self,Store_name,location):
        self.Store_name=Store_name
        self.location=location
        
    
        
c=coustomer2("faizal")
c.getter_data("Faizal_general_Store","kandivali")
print(f"the onwer name is {c.name} Store name is {c.Store_name} and location is {c.location}")
        


class emp:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def get_data(self,id,address):
        self.id=id
        self.address=address
        
w=emp("Raja",12000)
w.get_data("ES1230","Virar_West")
print(f"the name of an employee {w.name} salary is {w.salary} id is {w.id} and address is {w.address}")


class stud:
    def set_name(self,name):
        self.name=name
        
    def set_id(self,id):
        self.id=id
        
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    

f=stud()
f.set_name("rahul")
f.set_id(12345)
print(f"name is {f.get_name()} id is {f.get_id()}")


print("Get out of here Bob, we don\'t want no trouble.")
print("Get out of here Bob, we don't want no trouble.")