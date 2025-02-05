parrot= "Now"

for character in parrot: #does it until there is nothing more in "__"
    print(character)

number = "9,223.954;934:234 345"
separators=" "
for char in number:
    if not char.isnumeric():
        seperators=seperators+char

print(separators)
