fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newFruitList = []

for x in fruits:
    if "a" in x:
        newFruitList.append(x)
print(newFruitList)

print("Another short way: ")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

list1 = ["cherry", "mango", "pineapple", "papaya", "apple", "banana"]

list1.sort() #sort Acending
print(list1)

list1.sort(reverse=True) #sort Decending
print(list1)

print("Sort the case sensitive items: ")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

print("Copy the list: ")

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

print("Another way to Copy the list: ")

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


print("Another way to Copy the list using index: ")

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


print("List join: ")

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

print("Another way to List join using append: ")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
   list1.append(x)
print(list1)


print("Another way to List join using extend: ")

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

/*
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
*/