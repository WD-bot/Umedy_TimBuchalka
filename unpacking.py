a=b=c=d=e=f=32
print(c)

x, y, z=1,2,55
print(y)
print(z)

print("Unpacking a tuple")
data=1,6,55 # data represents a tuple which are immutable
# but tuples can always be unpacked
x,y,z=data
print(x)
print(y)
print(z)

print("Unpacking a list")
data_list=[15,18,20] # represents list _ mutable
data_list.append(14) # can't append while unpacking
# otherwise need to append more variables ex. s,t,u
p,q,r=data_list
print(p)
print(q)
print(r)
