import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(range(1, N + 1))

for j in range(M):
    a, b = map(int, sys.stdin.readline().split())
    it = b - a + 1
    for k in range(it // 2):
        if b > a:
            tmp = arr[a - 1]
            arr[a - 1] = arr[b - 1]
            arr[b - 1] = tmp
            b -= 1
            a += 1

print(arr)
