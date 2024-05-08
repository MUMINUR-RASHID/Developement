class Gadget:
    def __init__(self, brand, price, color, origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def __repr__(self):
        return f"Gadget: Brand: {self.brand}, Price: {self.price}, Color: {self.color}, Origin: {self.origin}"


class laptop(Gadget):
    def __init__(self, brand, price, color, origin, processor, ram, ssd, hdd):
        self.ram = ram
        self.ssd = ssd
        self.hdd = hdd
        self.processor = processor
        super().__init__(brand, price, color, origin)

    def __repr__(self):
        return f"Laptop: {super().__repr__()}, Processor: {self.processor}, RAM: {self.ram}, SSD: {self.ssd}, HDD: {self.hdd}"


class phone(Gadget):
    def __init__(self, brand, price, color, origin, ram, camera):
        self.ram = ram
        self.camera = camera
        super().__init__(brand, price, color, origin)

    def __repr__(self):
        return f"Phone: {super().__repr__()}, RAM: {self.ram}, Camera: {self.camera}"

    

phones=[]
laptops=[]

oppo=phone("OPPO",40000,"Black & White", "India","6gb & 8gb","32 mpx")
redme=phone("REDME",30000,"Black & White", "India","6gb & 8gb","16 mpx")
realme=phone("REALME",35000,"Black & White", "India","6gb & 8gb","32 mpx")
iPhone=phone("iPhone",80000,"Black & White", "China","6gb & 8gb","32 mpx")

phones.extend([oppo,redme,realme,iPhone])

Acer=laptop("ACER", 60000, "RGB", "USA", "I7 8gen", "8gb", "1TB", "2TB")
Hp=laptop("HP", 70000, "RGB", "USA", "AMD 5", "8gb", "1TB", "1TB")
Asus=laptop("ASUS", 65000, "RGB", "CHINA", "I5 8gen", "8gb", "500gb", "2TB")
Walton=laptop("WALTON", 60000, "RGB", "USA", "I7 8gen", "8gb", "1TB", "2TB")

laptops.extend([Acer,Hp,Asus,Walton])

print("----------WELCOME TO MY GADGET SHOP----------\n\n")

print("----------OUR PHONES----------")
for item in phones:
    print(item)

print("----------OUR LAPTOPS----------")
for item in laptops:
    print(item)


print("----------THANK YOU----------")

