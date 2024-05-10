class shop:
    cart=[]     #static atribute/class atribute   shobai use korte parbe
    origin="Chin"  # static atribute/class atribute

    def __init__(self,name,location):
        self.name="Jamu na"
        self.location="jam ar maje"

    def purchase(self, item,amount,price):
        remaining=amount-price
        print(f"Buying Item: {item}, for Price: {price}, Remaining: {remaining}")


    @staticmethod     #static e self dite pare na and class er self er kiso access/modify korte pare na

    def Multiply(a,b):
        print(a*b)
    

    @classmethod          #Class method object hishebe + alada function hishebe use kora jay
    def AC_hawa(self,item):
        print("AC er Hawa Khaitesi")

        

shopping=shop("Bashundhara","Dhaka")
shopping.AC_hawa("Lungi")