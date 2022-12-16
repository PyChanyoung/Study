def countingSort(array):
    answer = []
    count = [0] * (max(array)+1)

    for i in array:
        count[i] += 1

    for idx, val in enumerate(count):
        for j in range(val):
            answer.append(idx)
    return answer


arr = [8, 5, 2, 9, 5, 6, 3, 1, 1, 9]
print(countingSort(arr))
