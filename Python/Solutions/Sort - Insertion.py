def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1
    return array


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(insertionSort(array))
