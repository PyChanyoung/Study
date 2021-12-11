def bubbleSort(array):
    isSorted = False
    count = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array)-1-count):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                isSorted = False
        count += 1
    return array


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(bubbleSort(array))
