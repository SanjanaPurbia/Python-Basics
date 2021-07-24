class employee:
    count = 0
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
        employee.count += 1

emp1=employee("sanjana",50000)
emp2=employee("sonu",35000)
emp=employee("sanjana",50000)
emp3=employee("sonu",35000)

print("{} has salary {}".format(emp1.name,emp1.sal))
print("{} has salary {}".format(emp.name,emp.sal))
print("{} has salary {}".format(emp2.name,emp2.sal))
print("{} has salary {}".format(emp3.name,emp3.sal))
print("total no of employee= ",employee.count)