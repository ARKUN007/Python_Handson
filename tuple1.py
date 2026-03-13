tuple1 = ("apple", "banana", "cherry")
print(tuple1)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

print(len(thistuple))

thistuple1 = ("apple", )
print(thistuple1)

tuple2 = ("abc", 34, True, 40, "male")
print(tuple2)

print(type(tuple2))


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

if "apple" in thistuple:
    print("yes! apple in this fruit tuple")

tupleToList = list(thistuple)
print("tuple is now became list: ")
print(tupleToList)

print("changes in the list: ")

tupleToList.append("grapes")
print(tupleToList)

ListToTuple = tuple(tupleToList)
print("List became tuple noow: ")
print(ListToTuple)

#Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)

z = thistuple+y
print(z)

list_tuple = list(z)
print(list_tuple)

list_tuple.remove("banana")

tuple_list = tuple(list_tuple)
print(tuple_list)

thistuple = ("apple", "banana", "cherry")
try:
    del thistuple
    print("this tuple is deleted") #this will raise an error because the tuple no longer exists
except:
    print("Tuple is deleted")

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# Create the tuple
fruits = ("apple", "banana", "cherry")

# Print the second item
print(fruits[1])

# Print the number of items
print(len(fruits))

# Unpack the tuple
(a, b, c) = fruits

# Print b
print(b)