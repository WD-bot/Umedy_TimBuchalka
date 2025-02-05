#data=[3,5,28,456,23,356,29,289,160,50,390,380,43,234,654,678]
#data=[3, 5, 23, 28, 29, 43, 50, 160, 234, 289, 356, 380, 390]
# data=[160, 234, 289, 356, 380, 390, 456, 654, 678]
# data=[160, 234, 289, 356, 380, 390]
# data=[456, 654, 678,1029,3432,500,600,104]
data=[]
data.sort()

print(data)

# del data[0:2]
# print(data)
#
# del data[10:]
# print(data)

min_valid=100
max_valid=400

# process the low values in the list
stop=0
for index,value in enumerate(data):
    if value >= min_valid:
        stop =index
        break
print(stop) #for debugging
del data [:stop]
print(data)

#process high values of list
start=0
for index in range(len(data)-1,-1,-1):
    if data[index]<= max_valid:
        # we have the last we want to keep
        #set ´start´to the position of the first
        #item to delete which is the 1 after índex
        start=index +1
        break
print(start) #for debugging
del data [start:]
print(data)