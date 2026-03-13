list1 = ["apple", "banana", "cherry"]
list2 = ["mango", "pineapple", "papaya"]
list1.extend(list2)
print(list1)

list1.remove("banana")

print(list1)

list1.pop(1) #pop(1) will remove item to specific index
print(list1)

list1.pop() #pop() it will remove item from the last index
print(list1)

#del keyword also remove item from specified index

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
#del thislist -- this line will throw error
# this will remove the list completely
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear() # clear() will remove the items from the list only, but empty list will be there
print(thislist)

thislist = ["apple", "banana", "cherry", "mango", "pineapple", "papaya"]

for x in thislist:
    print(x)

print("Print all items by referring to their index number for loop:")   

for i in range(len(thislist)):
    print(thislist[i])

print("Print all items by referring to their index number while loop:")

i = 0
while i < len(thislist):
    print(thislist[i])
    i +=1

print("Short hand for loop: ")

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]