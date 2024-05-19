import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
V = int(sys.stdin.readline())
cnt = 0
for i in range(N):
    if arr[i] == V:
        cnt += 1
print(cnt)
