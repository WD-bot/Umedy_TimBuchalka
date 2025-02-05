pc_part=["computer",
         "monitor",
         "keyboard",
         "mousemat",
         "mouse"]
another_list= pc_part
print(id(pc_part))
print(id(another_list))

pc_part+=["list"] #change it all
print(id(pc_part))
print(id(another_list))
print((another_list))
a=b=c=d=f=another_list
print(a)
print("Adding creame")
b.append("cream") #means that "cream" is appending to list "b"
print(b)
print(c)