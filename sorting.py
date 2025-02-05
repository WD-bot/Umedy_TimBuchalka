pangram= "The quick brown fox jumps over the lazy dog"
not_pangram="The quick brown fox jumped over the lazy dog"
letters=sorted(pangram)
print(letters) #capitals will appear first afterwards
# alfabetical and with dublicates

numbers=[2.3,4.5,8.7,3.1,9.1,1.6]
sorted_numbers=sorted(numbers)
print(sorted_numbers) #sorted list
print(numbers) # old list

numbers.sort()
print(numbers) #if not used with another variable
# it changes the order in and of the original list NO dublicates

missing_letter=sorted(not_pangram,key=str.casefold)
print(missing_letter)

names=["Graham","John","terry","eric","Terry","michael"]
names.sort(key=str.casefold)
print(names)
