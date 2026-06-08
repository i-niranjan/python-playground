class BaseChai:

    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai...")

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamon, ginger, cloves")

chai = MasalaChai("Masala")

chai.add_spices()


## composition

class ChaiShop:
    chai_clas = BaseChai

    def __init__(self):
        self.chai = self.chai_clas("Regular")




