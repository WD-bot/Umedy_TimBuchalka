# for index, character in enumerate("abcdefgh"): #enumarate lægger numre til karakterne
#     print(index, character)

for t in enumerate("abcdefgh"): #we get it in a tuple
    index, character=t
    print(index, character)

print()
index, character=(0,'a')
print(index) #0
print(character) #a
