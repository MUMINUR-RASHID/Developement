class MyPens:
    def __init__(self, PenName, Amount, Price):
        self.PenName = PenName
        self.Amount = Amount
        self.Price = Price

    def quality(self):
        if self.Price > 100:
            return f"{self.PenName} is a Good Quality Pen"
        else:
            return f"{self.PenName} is a Normal Pen"


pen1 = MyPens("Montax", 10, 150)
q1 = pen1.quality()
print(q1)

pen2 = MyPens("Matador", 10, 70)
q2 = pen2.quality()
print(q2)

pen3 = MyPens("Labyrinth", 10, 120)
q3 = pen3.quality()
print(q3)
