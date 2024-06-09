N, M = map(int, input().split())
arr = []
def color(i,j):
    ans=0
     for k in range(8):
            for l in range(8):
                arr[i+k][j+l]


for i in range(M):
    arr.append(list(input()))
cnt = 2**31 - 1
for i in range(N - 7):
    for j in range(M - 7):
        if cnt > color(i, j):
            cnt = color(i, j)
print(cnt)
