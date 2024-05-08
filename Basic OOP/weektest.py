class Product:
    def __init__(self,name,price,amount):
        self.name=name
        self.price=price
        self.amount=amount

    def __repr__(self) -> str:
        return f"{self.name} {self.price} per kg, weight {amount} kg, cost {self.price*self.amount} Taka"


class Shop():
    products={"piaj":60, "alu":20, "tomato":30, "begun":15, "oil":90, "kacha morich":140}
    def __init__(self, name):
        self.name=name
        self.cart=[]
        self.total=0

    def add_product(self,product,amount):

        price=self.products[product]

        self.total+=(amount*price)
        pr=f"{Product(product,price,amount)}, Total {self.total} Taka"
        self.cart.append(pr)


    def buy_product(self,product):
        if product in self.products:
            return True
        else:
            return False
        
    def checkout(self,taka):
        if taka>self.total:
            print("Here is Your Products")
            extra=taka-self.total
            print(f"Here is Your Extra {extra} Taka.")
            return extra*-1
        
        elif taka<self.total:
            extra=self.total-taka
            self.total=extra
            print(f"Please give {extra} Taka More.")
            return extra
        
        else:
            print("Here is Your Products")
            return 0
        


name=input("What is your name?: ")

name_obj=Shop(name)

print(f"\nOur available products are {name_obj.products}\n")
while True:
    check=input("Do you need any product? (yes/no): ")

    if check=="yes":
        product=input("which product you want?: ")

        isProduct=name_obj.buy_product(product)

        if isProduct:
            amount=int(input("Congratulatio! product is not available. How much do you want (in kg)?: "))
            name_obj.add_product(product,amount)
        else:
            print("Sorry  this product is not available.")

    else:
        break


print("\n----------Mr. {name} Your shopping List is----------")
for st in name_obj.cart:
    print(st)


print(f"\nYour Total bill is {name_obj.total}")

check=True
while check:
    taka=int(input("Please Pay The Bill: "))
    ex=name_obj.checkout(taka)
    if ex<=0:
        check=False
    else:
        check=True


print(f"\n----------Thank you Mr. {name} for Shopping----------")

