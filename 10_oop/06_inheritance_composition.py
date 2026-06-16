class BaseChai:

    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai...")

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamon, ginger, cloves")



## composition

class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        self.chai.prepare()
        print(f"Serving {self.chai.type} chai in the shop")


class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai



fancy = FancyChaiShop()


fancy.chai_cls.add_spices(fancy.chai)
# fancy.chai.add_spices()
fancy.serve()





