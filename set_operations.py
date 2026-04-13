myset = {"apple", "banana", "cherry"}

print(myset)

setToList = list(myset)

setToList.append('mango')

myset = set(setToList)

print(myset)

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)