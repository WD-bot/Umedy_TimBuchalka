age=int(input("How old are you?" ))

#if age >=16 and age <=65: #between 16 and 65
if 16<=age<=65: #simpler way of writing
    print("Enjoy your work today")
else:
    print("enjoy your day")

print("_"*80)

if age <16 or age >65: #with "or" instead
    print("enjoy your free time")
else:
    print("Enjoy your work today")

