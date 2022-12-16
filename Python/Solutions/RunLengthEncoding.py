def runLengthEncoding(string):
    answer = []
    current = 1
    for i in range(1, len(string)):
        if string[i-1] != string[i] or current == 9:
            answer.append(str(current) + string[i-1])
            current = 0
        current += 1

    answer.append(str(current) + string[-1])
    return ''.join(answer)


print(runLengthEncoding('AAAAAAAAAAAAABBCCCCDD'))
