def getRow(rowIndex):
    arr = [[1]]
    for i in range(rowIndex):
        arr2 = [1]
        for j in range(len(arr[i]) - 1):
            num = arr[i][j] + arr[i][j + 1]
            arr2.append(num)

        arr2.append(1)
        arr.append(arr2)

    return arr[rowIndex]
