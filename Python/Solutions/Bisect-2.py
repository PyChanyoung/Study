# Solution 2 : O(logN)
def bisect(arr, x):
    if binary_search_start(arr, x) == -1:
        return -1
    return binary_search_end(arr, x) - binary_search_start(arr, x) + 1


def binary_search_start(array, target):
    start, end = 0, len(array) - 1
    startIdx = -1
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            startIdx = mid
            end = mid - 1
        elif array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return startIdx


def binary_search_end(array, target):
    start, end = 0, len(array) - 1
    EndIdx = -1
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            EndIdx = mid
            start = mid + 1
        elif array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return EndIdx


arr = [1, 2, 2, 2, 4, 4, 4, 4, 4]
x = 2
print(bisect(arr, x))
