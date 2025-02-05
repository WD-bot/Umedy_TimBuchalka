for i in range(1,4):
    print("no. {} squared is {} and cubed is {}".format(i,i**2,1**3))
    print("_"*60)

name=input("Please enter your name")
age=int(input("How old are you, {0}?".format(name)))
print(name,"is", age)

# if age >=18:
#    print("You're old enough to vote")
#    print("Please put an X in the box")
#else:
#    print("You can't vote. Please come back in {0} years".format(18-age))

if age <18:
    print("You can't vote. Please come back in {0} years".format(18-age))
elif age ==900:
    print("No is just your craziness head kicking in <3")
else:
    print("You're old enough to vote")
    print("Please put an X in the box")