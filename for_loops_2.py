#number = "9,223.954;934:234 345"
number=input("please but any number of your choosing and any separators as well :)")
separators=""
for char in number:
    if not char.isnumeric():
        separators=separators+char

#print(separators)
#print(char)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
print(sum([int(val) for val in values]))

print("___"*60)
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.

for char in quote:
    if char.isupper():
        print(char)