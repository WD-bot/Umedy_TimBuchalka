# result=True
# another_result=result
# print(id(result))
# print(id(another_result))
#
# result=False

result="Correct"
another_result= result
print(id(result))
print(id(another_result))

result += "ish" # doesnt change anything
print(id(result))
print(id(another_result))
