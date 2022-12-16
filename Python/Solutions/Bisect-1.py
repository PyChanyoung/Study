from bisect import bisect_left, bisect_right


def bisect(arr, x):
    print('bisect_right: ', bisect_right(arr, x))
    print('bisect_left: ', bisect_left(arr, x))
    return bisect_right(arr, x) - bisect_left(arr, x)


arr = [1, 1, 2, 2, 2, 2, 3]
x = 2
print(bisect(arr, x))
