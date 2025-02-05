       #012345678910
parrot="Norwegian Blue"

print(parrot)
print(parrot[3],parrot[-1],parrot[9],parrot[3],parrot[6],parrot[8])


print(parrot[-11],parrot[-1],parrot[-5],parrot[-11],parrot[-8],parrot[-6]) #tæller bagfra e=-1 N=-14
print((parrot[3-14]),(parrot[4-14]),(parrot[9-14]),(parrot[3-14]),(parrot[6-14]),(parrot[8-14]))
print(parrot[3-14],parrot[4-14],parrot[9-14],parrot[3-14],parrot[6-14],parrot[8-14])

print(parrot[0:6]) #does not include the sixed index
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])

print(parrot[10:14])
print(parrot[10:])

print(parrot[0:6:2])
print(parrot[1:4:2])

nummer="9,435:345,454;123*567"
seperators=nummer[1::4]

print(seperators)

letters ="abcdefghijklmnopqrstuvwxyz"
backwards=letters [25::-1]
print(backwards)

qpo=letters [16:13:-1]
print(qpo)

edcba=letters [4::-1]
print(edcba)

toge=qpo+edcba
print(toge)

print(toge[::-1])

greeting="Hello "
name = "Olivia "
age = "25 "
print(greeting+name)

print(age)
print(type(greeting))
print(type(age))

age_in_words="25 years"
print(name +f"is {age} years old") #f-string

print(f"Pi is approximatly {22/7:12.50f}")
pi=22/7
print(f"Pi is approximatly {pi:12.50f}") #med variable

print("spam" + "eggs"+ "beans")
print("spam, eggs, beans")
print("""spam
eggs
beans""")
print("spam /n eggs /n beans")

quan=10
price=5.0
total=quan*price
print(total)


days="1:a, 2:b, 3:c, 4:d, 5:e"
print(days[0:-1:5])
