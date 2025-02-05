#for i in range(21,4,-3):
    #print("The index is now{}".format(i))
age=int(input("How old are you?"))

if age in range(16,66):
    print("Enjoy your work today")
else:
    print("enjoy your free time")

print("_"*80)

if age <16 or age >65: #with "or" instead
    print("enjoy your free time")
else:
    print("Enjoy your work today")

