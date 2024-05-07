class shop:
    def __init__(self,Name):
        self.name=Name
        self.market=[]
    
    def items(self, item, Weight,price):
        product={"item":item, "Amount":Weight, "Price":price}
        self.market.append(product)

    def total(self):
        self.Total=0
        for item in self.market:
            self.Total+=item["Amount"]*item["Price"]
        print(f"{self.name}, your Total product Value is {self.Total} Taka.")
    
    def checkout(self,taka):
        if taka>self.Total:
            print("Here is Your Products")
            extra=taka-self.Total
            print(f"Here is Your Extra {extra} Taka.")
            return extra*-1
        
        elif taka<self.Total:
            extra=self.Total-taka
            self.Total=extra
            print(f"Please give {extra} Taka More.")
            return extra

        else:
            print("Here is Your Products")
            return 0
        
    def rem(self, item, Weight,price):
        for it in self.market:
            if it["item"]==item:
                self.Total-=it["Amount"]*it["Price"]
                self.market.remove(it)
        product={"item":item, "Amount":Weight, "Price":price}
        self.market.append(product)
        self.Total+=(Weight*price)
        print(f"{self.name}, your Total product Value is {self.Total} Taka.")



#This portion can be change with user input


shachin=shop("Shachin")
shachin.items("Alu",6,10)
shachin.items("Tomato",2,15)
shachin.items("Piaj",2,60)
shachin.items("Kacha morich",1,150)

shachin.total()

ans=input("Do you want to remove anything? ")

if ans=="yes":
    shachin.rem("Tomato",1,15)


check=True
while check:
    taka=int(input("Please Pay The Bill: "))
    ex=shachin.checkout(taka)
    if ex<=0:
        check=False
    else:
        check=True





print("Thank You")
