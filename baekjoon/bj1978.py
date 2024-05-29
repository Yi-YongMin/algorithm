tc = int(input())
arr = list(map(int, input().split()))
cnt = 0
ans = 0
for i in range(tc):
    if arr[i] == 1:
        continue
    elif arr[i] == 2:
        cnt += 1
        continue
    factor = 1
    while factor <= arr[i] / 2:
        factor += 1
        if arr[i] % factor == 0:
            ans = 1
            break
    if ans == 1:
        ans = 0
    elif ans == 0:
        cnt += 1
print(cnt)
