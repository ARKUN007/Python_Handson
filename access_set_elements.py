thisset = {"apple", "banana", "cherry"}

for i in thisset:
    print(i)

print("banana" in thisset)

print("banana" not in thisset)

print("Adding new element to the set: ")
thisset.add("mango")
print(thisset)


print("adding two sets :")

thisset1 = {"apple", "banana", "cherry"}
tropical1 = {"pineapple", "mango", "papaya"}

thisset1.update(tropical1)

print(thisset1)


print("Adding list to the set: ")
thisset2 = {"apple", "banana", "cherry"}
mylist2 = ["kiwi", "orange"]

thisset2.update(mylist2)

print(thisset2)

print("Removing element from the set using 'remove': ")
thisset3 = {"apple", "banana", "cherry"}

thisset3.remove("banana") #if item is not present in set then remove will throw error.

print(thisset3)

print("Removing element from the set using 'discard': ")
thisset4 = {"apple", "banana", "cherry"}

thisset4.discard("apple") #if item is not present in set then discard will not throw any error.

print(thisset4)


print("Removing element from the set using 'pop': ")
thisset5 = {"apple", "banana", "cherry"}
x = thisset5.pop() #pop will remove element randomly.
print(x)
print(thisset5)

print("Removing element from the set using 'clear': ")
thisset6 = {"apple", "banana", "mango"}
thisset6.clear() #clear() will remove all the elements at once.
print(thisset6)

print("Deleting set using 'de' : ")
thisset7 = {"apple", "banana", "mango", "litchi"}
del thisset7
print(thisset7)

      

