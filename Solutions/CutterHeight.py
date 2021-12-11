# 나동빈의 풀이
# O(N logN) for Time
# O(1) for Space
# 커터의 숫자는 따로 정렬할 필요가 없이 이미 연속된 수로서 정렬된 상태이다. (ex. 0 ~ 19)

def cutter(array, m):
    start, end = 0, max(array)
    cutterHeight = 0

    while start <= end:
        mid = (start+end) // 2
        total = 0
        for num in array:
            current = num - mid
            if current > 0:
                total += current
        if total < m:
            end = mid-1
        else:
            cutterHeight = mid
            start = mid+1

    return cutterHeight

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19


m = 6
arr = [19, 15, 10, 17]
print(cutter(arr, m))
