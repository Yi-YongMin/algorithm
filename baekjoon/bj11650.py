N = int(input())
arr = []
for i in range(N):
    x, y = map(int, input().split())
    arr.append([x, y])
arr.sort(key=lambda x: (x[0], x[1]))
for i in range(N):
    print(arr[i][0], arr[i][1])
