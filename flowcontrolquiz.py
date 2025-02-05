# value = 8
# answer = 0
#
# for x in range(1, 13):
#     answer = value * x
#     print("{0} times {1} is {2}".format(x, value, answer))

# for x in range(30):
#     if x % 3 == 0 or x % 5 == 0:
#         continue
#     print(x)
#
# for x in range(30):
#     if x % 3 != 0 and x % 5 != 0:
#         print(x)

choice = None

while choice != '0':
    choice = input("Please enter your choice.  Press enter to quit")
    if choice == '':
        break

    print("You have selected {}".format(choice))
else:
    print("Thank you for playing, please call back soon.")