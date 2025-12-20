class Person:
    def __init__(self, name, id_num):
        self.name = name
        self.id_num = id_num
    def display(self):
        print(self.name)
        print(self.id_num)

class Employee(Person):
    def __init__(self, name, id_num, salary, post):
        self.salary = salary
        self.post = post
        #Person.__init__(self, name, id_num)
        super().__init__(name, id_num)

a = Employee("Bob", 676767, 500000, "Manager")
a.display()
