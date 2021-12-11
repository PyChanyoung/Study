def quickSort(array):
    quickSortHelper(array, 0, len(array)-1)
    return array


def quickSortHelper(array, start, end):
    if start > end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        if array[left] > array[pivot] or array[pivot] > array[right]:
            array[left], array[right] = array[right], array[left]
        if array[left] <= array[pivot]:
            left += 1
        if array[pivot] <= array[right]:
            right -= 1
    array[pivot], array[right] = array[right], array[pivot]

    leftSmall = right - 1 - start < end - (right + 1)

    if leftSmall:
        quickSortHelper(array, start, right - 1)
        quickSortHelper(array, right + 1, end)
    else:
        quickSortHelper(array, right + 1, end)
        quickSortHelper(array, start, right - 1)


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(quickSort(array))
