# 6, 12, 18, 24
T = int(input())
N = 1
cnt = 1
while True:
    N = N + 6 * cnt
    if N >= T:
        cnt += 1
        break
    else:
        cnt += 1
if T == 1:
    cnt = 1
print(cnt)
