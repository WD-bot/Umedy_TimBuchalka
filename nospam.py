menu= [
    ["eggs","bacon"],
    ["eggs", "sausage","bacon"],
    ["eggs","spam"],
    ["eggs", "bacon", "spam"],
    ["eggs", "sausage", "bacon", "spam"],
    ["spam","eggs", "spam", "eggs", "bacon", "spam"],
    ["spam", "sausage","spam", "bacon", "spam", "tomato", "spam"]
] #nested lists
for meal in menu:
    for index in range(len(meal)-1,-1,-1): #going backwards
        if meal[index] =="spam":
            del meal[index] #del is used in lists this way
    else:
        print(", ".join(meal))

# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item, end=", ")
#     print()


# for meal in menu:
#     if "spam" not in meal:
#         print(meal)
#
#         for item in meal:
#             print(item)
#     else:
#         remove("spam")