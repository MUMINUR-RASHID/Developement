class person:
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height

    def eat(self):
        print("Eating Vat,polaw,Mangsho")

    def exercise(self):
        raise NotImplementedError

class cricketer(person):
    def __init__(self, name, age, weight, height,team,hour):
        self.team=team
        self.hour=hour
        super().__init__(name, age, weight, height)


    #Override
    def eat(self):
        print("I am eating Vegitables & Fruits")

    #override
    def exercise(self):
        print("I am Exercising")


    #overloading
    def __add__(self,other):
        return f"Our Combine Exercise Hours are {self.hour+other.hour}"
    
    #overloading
    def __mul__(self,other):
        return f"Our Multiple Exercise Hours are {self.hour*other.hour}"



Sakib=cricketer("Shakib",38,70,68,"BANGLADESH",3)
Mushi=cricketer("Mushofiq",36,68,66,"BANGLADESH",4)
Sakib.eat()
Sakib.exercise()

print(Sakib+Mushi)
print(Sakib*Mushi)