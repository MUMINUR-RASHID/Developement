#Method Practice




class calculation:
    def add(self, num1, num2):
        result=f"The Addition Result Is {num1+num2}"
        return result
    
    def sub(self, num1, num2):
        result=f"The Substructed Result Is {num1-num2}"
        return result
    

    def mul(self, num1, num2):
        result=f"The Multiplication Result Is {num1*num2}"
        return result
    

    def div(self, num1, num2):
        result=f"The Divition Result Is {num1/num2:.{3}f}"
        return result
    


num1=int(input("give the first number: "))
num2=int(input("give the second number: "))
calculator=calculation()
addition= calculator.add(num1, num2)
substruction=calculator.sub(num1,num2)
multiplication=calculator.mul(num1,num2)
divition=calculator.div(num1,num2)

print(addition)
print(substruction)
print(multiplication)
print(divition)