def removeprefix(string:str, prefix:str)-> str:
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:] #returns a copy of the string


def removesuffix(string: str, suffix:str)->str:
    if suffix and string.endswith(suffix): #suffix='' should not call string[:-0]
        return string [:-len(suffix)]
    else:
        return string[:]



filename = 'hungrydane.txt'
with open(filename) as poem:
    first= poem.readline().rstrip()

print(first)

chars = "'The!"
# no_apostrophe = first.strip(chars)
# print(no_apostrophe)

for character in first:
    if character in chars:
        print(f"removing {character}")
    else:
        break
print('*'*80)
for character in first [::-1]: #backwards
    if character in chars:
        print(f'removing"{character}"')
    else:
        break
print('*'*80)
# the_removed=first.removesuffix("'The") # doesnt work for this python
the_removed = removeprefix(first,"'The")
print(the_removed)
# dane_removed=first.removeprefix("Dane!")
dane_removed=removesuffix(first,"Dane!")
print(dane_removed)

