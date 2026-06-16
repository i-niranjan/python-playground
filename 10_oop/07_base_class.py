class Chai:

    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


# Code duplication
# class GingerChai(Chai):

#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level

# Accessing base class constructor using explicit call of inheritance

# class GingerChai(Chai):

#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self,type_,strength)
#         self.spice_level = spice_level

#Accessing base class constructor using super method

class GingerChai(Chai):

    def __init__(self, type_, strength, spice_level):
        super().__init__(type_,strength)
        self.spice_level = spice_level

