data=[104,101,4,105,308,103,7,107,100,306,106,102,108,700,204,176,180]
min_valid=100
max_valid=200

# for index in range(len(data)-1,-1,-1): #-1'erne gør at det går baglæns
#     if data[index]<min_valid or data[index]> max_valid: #udvælgelsesproces
#         # ift min og max værdi
#         print(index, data)
#         del data[index] #sletter data
#
# print(data)
top_index=len(data)-1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index-index,value)
        del data[top_index-index]
print(index, value)
data.sort()
print(data)