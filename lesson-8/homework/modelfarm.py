class ParentAnimal:
    def __init__(self,name,type):
        self.name=name
        self.type=type

    def walk(self):
        return f"{self.type}:{self.name} is walking"
    def eat(self):
        return f"{self.type}:{self.name} is eating"
    def sleep(self):
        return f"{self.type}:{self.name} is sleeping"
    
    
class Animal1(ParentAnimal):
    def __init__(self,name,type):
        super().__init__(name,type)
    def walking(self):
        return super().walk()

class Animal2(ParentAnimal):
    def __init__(self,name,type):
        super().__init__(name,type)
    def eating(self):
        return super().eat()

class Animal3(ParentAnimal):
    def __init__(self,name,type):
        super().__init__(name,type)
    def sleeping(self):
        return super().sleep()

    

a1=Animal1("Cat","Mosh")
a2=Animal2("Cow","Sigirvoy")
a3=Animal3("Sheep","B")

print(a1.walking())
print(a2.eating())
print(a3.sleeping())
