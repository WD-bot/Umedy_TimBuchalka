pc_parts=["computer",
         "monitor",
         "keyboard",
         "mousemat",
         "mouse"]

print(pc_parts)
pc_parts[3]="VHS" #replaces the item 3 in the list
print(pc_parts[3:])
pc_parts[3:]="trackball"
print(pc_parts)

pc_parts[3:]=["trackball"]
print(pc_parts)

