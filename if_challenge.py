name=input("What is your name?")
age=int(input("Hello {}, how old are you?".format(name)))

if 17< age < 31:
    print("Welcome to the holiday at Ibiza, {}!".format(name))
else:
    print("Sorry, hope you have a great summer")
