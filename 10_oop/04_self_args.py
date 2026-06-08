class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml chai cup"

cup = Chaicup()
cup.size ="10"
print(Chaicup.describe(cup))