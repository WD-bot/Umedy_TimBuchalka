empty_list=[]
even=[2,4,6,8,10]
odd=[1,3,5,7,9]

numbers =even+odd
print(numbers)

numbers=[even, odd] #makes a list with 2 lists
print(numbers)

for number_list in numbers:
    print(number_list)
    for value in number_list:
        print(value)


# sorted_numbers=sorted(numbers)
# print(sorted_numbers)
# print(numbers)
#
# digits=list("1456820443678")
# print(digits)
#
# # more_numbers=list(numbers)
# # more_numbers =numbers[:]
# more_numbers = numbers.copy()
# print(more_numbers)
# print(numbers is more_numbers) #not the same list, so if variables turn to the same list
# print(numbers == more_numbers) # but copy/identical , so contains the same numbers
# even.extend(odd)
# print(even)
# another_even=even
#
# even.sort()
# print(even)
# even.sort(reverse=True)
# print(even)
# print(another_even)

# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
#
# print()
# print(len(even))
# print(len(odd))
# print()
# print("mississippi".count("issi"))

