N = int(input())
arr = []
for i in range(N):
    a, b = map(str, input().split())
    a = int(a)
    arr.append([a, b])
arr.sort(key=lambda x: (x[0]))
for i in range(N):
    print(arr[i][0], end=" ")
    print(arr[i][1])
