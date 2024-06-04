N, M = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 2**32 - 1
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            now = arr[i] + arr[j] + arr[k]
            diff = M - now
            if diff >= 0 and cnt >= diff:
                cnt = diff
print(M - cnt)
