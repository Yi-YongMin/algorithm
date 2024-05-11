import sys

N = int(sys.stdin.readline())
for i in range(N):
    ans = sys.stdin.readline()
    b = ans[len(ans) - 2]
    print(ans[0] + b)
