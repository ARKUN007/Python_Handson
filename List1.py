thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(thislist[3])
print(thislist[0:2])
print("Change list items")
thislist[4] = "kiwi"
print(thislist)

print("change rang of list items")

thislist[0:2] = ["fruit1", "fruit2"]

print(thislist)

print("Insert new item without replacing of the existing item")

thislist.insert(2,"Fruit3") #insert will add items to the specific index
print(thislist)

print("Add item in list at the end use append()")

thislist.append("last_item")
print(thislist)
