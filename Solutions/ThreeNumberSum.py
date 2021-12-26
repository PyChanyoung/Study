def threeNumberSum(array, targetSum):
    array.sort()
    answer = []
    for first in range(len(array)-2):
        second, third = first+1, len(array)-1
        while second < third:
            current = array[first]+array[second]+array[third]
            if current == targetSum:
                answer.append([array[first], array[second], array[third]])
                second += 1
                third -= 1
            elif current > targetSum:
                third -= 1
            else:
                second += 1
    return answer


array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
print(threeNumberSum(array, targetSum))
