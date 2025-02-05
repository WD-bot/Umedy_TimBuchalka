chosen_activity= "-"
# while True:
#     if chosen_activity== "0":
#         print("Have a good day!")
#         break
#     elif chosen_activity in "1234":
#         print("Nice that you did option {}".format(chosen_activity))
#     else:
#         print("Please choose from the list below. What would you like to do?")
#         print("1.\t Eat ")
#         print("2.\t Take a bath ")
#         print("3.\t Work out ")
#         print("4.\t Learn Python ")
#         print("0.\t Exit")
#     chosen_activity = input()


while chosen_activity != "0":
        print("Have a good day!")
    if chosen_activity in "1234":
        print("Nice that you did option {}".format(chosen_activity))
    else:
        print("Please choose from the list below. What would you like to do?")
        print("1.\t Eat ")
        print("2.\t Take a bath ")
        print("3.\t Work out ")
        print("4.\t Learn Python ")
        print("0.\t Exit")
    chosen_activity = input()
