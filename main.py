class Car:
    def __init__(self):
        self.marka = input("Cho za marka?")
        self.svet = input("Svet kakoi?")
        self.tipdvigatelya = input("Tip dvijka?")

    def drive(self):
        print("Yehal ya domoi s raboty")

    def __str__(self):
        return f"Marka mashini eto {self.marka}\n Svet mashini eto {self.svet}\n Tip dvigatelya eto {self.tipdvigatelya}\n "

jigul = Car()
print(jigul)
jigul.drive()




