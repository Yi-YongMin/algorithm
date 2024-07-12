N = int(input())
arr = list(map(int, input().split()))
M = int(input())
ans = list(map(int, input().split()))
for i in range(M):
    if ans[i] in arr:
        print("1", end=" ")
    else:
        print("0", end=" ")
