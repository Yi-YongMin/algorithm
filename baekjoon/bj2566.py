arr = [[] for _ in range(9)]
for i in range(9):
    arr[i] = list(map(int, input().split()))

tmp, row, col = 0, 0, 0
for i in range(9):
    for j in range(9):
        if tmp <= arr[i][j]:
            tmp = arr[i][j]
            row = i + 1
            col = j + 1
print(tmp)
print(str(row) + " " + str(col))
