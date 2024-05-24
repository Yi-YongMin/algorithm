N, M = map(int, input().split())
matrix1 = [[] for _ in range(N)]
matrix2 = [[] for _ in range(N)]
matrix3 = [[] for _ in range(N)]
for i in range(N):
    matrix1[i] = list(map(int, input().split()))
for i in range(N):
    matrix2[i] = list(map(int, input().split()))

matrix3 = [[matrix1[i][j] + matrix2[i][j] for j in range(M)] for i in range(N)]

for i in range(N):
    print(*matrix3[i])
