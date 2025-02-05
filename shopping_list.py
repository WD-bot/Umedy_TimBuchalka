#

#for item in shopping_list:
    #if item !="spam"
    #print("Buy "+item)

#for item in shopping_list:
   # if item == "spam":
      #  continue   #!!! continue

   # print("Buy " + item)


#for item in shopping_list:
   # if item == "spam":
       # break   #!!! break

  #  print("Buy " + item)

shopping_list=["milk","pasta","eggs","spam","bread","rice"]

item_to_find="spam"
found_at = None

# for index in range(6)
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
print("Item found at position {}" .format(found_at))