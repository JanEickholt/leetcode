def minOperations(boxes):
    answer = []
    length = len(boxes)
    for i in range(length):
        sum = 0
        for j in range(length):
            if boxes[j] != "0":
                sum += abs(i - j)
        answer.append(sum)

    return answer
