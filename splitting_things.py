panagram= """The quick brown fox jumps
 \tover the lazy dog"""
words=panagram.split()
print(words)

numbers="9,22,3,452,97,654,023,697,895"
print(numbers.split(", "))
# values="".join(char if char not in separators else " " for char in numbers).split()
generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
values = "".join(generated_list)
print(values)

values_list = values.split()
print(values_list)

# Use a for loop to produce a list of ints, rather than strings.
# You can either modify the contents of the 'values_list' list in place,
# or create a new list of ints.

#replaces values in place
for index in range(len(values_list)):
    values_list[index]= int(values_list[index])

print(values_list)

#making a new list
integer_values=[]
for value in values_list:
    integer_values.append(int(value))

print(integer_values)