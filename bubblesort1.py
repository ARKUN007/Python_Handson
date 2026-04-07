array1 = [7, 12, 9, 11, 3]

n = len(array1)

for i in range(n-1):
    for j in range(n-i-1):
        if array1[j] > array1[j+1]:
            array1[j], array1[j+1] = array1[j+1], array1[j]
print("sorted bubble array is :", array1)