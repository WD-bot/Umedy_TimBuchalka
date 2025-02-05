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
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(item)
    else:
        print("{0} has a spam score of {1}"
              .format(meal,meal.count("spam")))