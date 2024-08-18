class Employee:
    company="ABC"
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
class new_emp(Employee):
    def __init__(self,name,id,salary,address):
        super().__init__(name,id)
        self.salary=salary
        self.address=address
    
    def get_detail(self):
        print(f"the Employee name is {self.name} id is {self.id} salary is {self.salary} and address is {self.address} and company is {Employee.company}")


#e=Employee("Rahul",101)
e1=new_emp("Rahul",101,12000,"kandivali")

e1.get_detail()        