def selectionSort(array):
    for i in range(len(array)-1):
        minIdx = i
        for j in range(i+1, len(array)):
            if array[minIdx] > array[j]:
                minIdx = j
        array[minIdx], array[i] = array[i], array[minIdx]
    return array


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(selectionSort(array))
