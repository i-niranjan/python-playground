# # def make_chai():
# #     print("Here is your masala chai")

# # return_value = make_chai()

# # print(return_value)

# def idle_chaiwala():
#     pass

# print(idle_chaiwala())


# def sold_cups():
#     return 120

# total = sold_cups()
# print(total)

# def chai_status(cups_left):
#     if cups_left == 0:
#         return "Sorry, chai over"
#     return "chai is ready"

# print(chai_status(0))
# print(chai_status(5))

# def chai_report():
#     return 100, 20,30

# sold, remaining,_ = chai_report()
# print(sold)
# print(remaining)
# print(_)

# def pour_chai(n):
#     if n == 0:
#         return "All cups poured"
#     return pour_chai(n-1)

# print(pour_chai(5))

chai_types = ["light","kadak","ginger","kadak"]

strong_chai = list(filter(lambda chai : chai !="kadak", chai_types))

print(strong_chai)