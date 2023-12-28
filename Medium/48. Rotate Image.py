def rotate(matrix):
    if len(matrix) != 1:
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[i])):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        indexx = 0
        for i in matrix:
            matrix[indexx] = i[::-1]
            indexx += 1

