matrix = []


for i in range(5):
    row = input().split()   
    matrix.append(row)


for i in range(5):
    for j in range(5):
        if matrix[i][j] == '1':  
            row = i + 1
            col = j + 1


print(abs(row - 3) + abs(col - 3))