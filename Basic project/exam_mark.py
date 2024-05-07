import random


class Exam:
    def __init__(self, Name):
        self.name=Name
        self.total=0

    def bangla(self, attend):
        if attend==True:
            self.total+=random.randint(70,88)
        else:
            print(f"{self.name} is not attend in Bangla exam")

    def english(self, attend):
        if attend==True:
            self.total+=random.randint(75,90)
        else:
            print(f"{self.name} is not attend in English exam")

    def math(self, attend):
        if attend==True:
            self.total+=random.randint(80,98)
        else:
            print(f"{self.name} is not attend in Math exam")
    
    def total_mark(self):
        print(f"{self.name} got total marks {self.total}")




ratul=Exam("Ratul")
ratul.bangla(True)
ratul.english(True)
ratul.math(True)
ratul.total_mark()

tarek=Exam("Tarek")
tarek.bangla(True)
tarek.english(True)
tarek.math(False)
tarek.total_mark()

nipu=Exam("Nipu")
nipu.bangla(False)
nipu.english(True)
nipu.math(True)
nipu.total_mark()

jubair=Exam("Jubair")
jubair.bangla(True)
jubair.english(False)
jubair.math(True)
jubair.total_mark()