class employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.__money=salary


    #its a getter read only not changeable and using as a method
    def show_money(self):
        return self.__money
    

    @property      #its a getter read only not changeable and using as a atribute
    def show_sallary(self):
        return self.__money
    
    #setter use korte hole age oi method k getter korte hoy/atribute banaite hoy

    @property
    def change_salary(self):
        return self.__money
    
    @change_salary.setter
    def change_salary(self,amount):
        self.__money+=amount
    



sakib=employee("Shakib",38,40000)
print(sakib.show_money())  #method call
print(sakib.show_sallary)  #atribute call
sakib.change_salary=10000
print(sakib.change_salary)