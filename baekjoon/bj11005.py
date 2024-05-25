N, B = map(int, input().split())
cnt = 0
ans = []
while True:
    if N // B >= B:
        ans.insert(0, N % B)
        N = N // B
        cnt += 1
    elif N // B < B:
        if N // B != 0:
            ans.insert(0, N % B)
            ans.insert(0, N // B)
            cnt += 2
        else:
            ans.insert(0, N % B)
            cnt += 1
        break
# print(cnt)
for i in range(cnt):
    if ans[i] >= 10:
        ans[i] = chr(ans[i] + 55)
print(*ans, sep="")
