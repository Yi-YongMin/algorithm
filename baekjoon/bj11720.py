import sys

N = int(sys.stdin.readline())
arr = sys.stdin.readline()
ans = 0
for i in range(N):
    ans += int(arr[i])
print(ans)
