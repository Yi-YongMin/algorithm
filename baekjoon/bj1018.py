N, M = map(int, input().split())
arr = []


def color(i, j):
    ans1, ans2 = 0, 0
    for k in range(8):
        for l in range(8):
            if k % 2 == 0 and l % 2 == 0 and arr[i + k][j + l] != arr[i][j]:
                ans1 += 1
            elif k % 2 == 1 and l % 2 == 1 and arr[i + k][j + l] != arr[i][j]:
                ans1 += 1
            elif k % 2 == 1 and l % 2 == 0 and arr[i + k][j + l] == arr[i][j]:
                ans1 += 1
            elif k % 2 == 0 and l % 2 == 1 and arr[i + k][j + l] == arr[i][j]:
                ans1 += 1
    for k in range(8):  # 현재 자리를 리버스로 색칠했을 때.
        for l in range(8):
            if (
                k % 2 == 0 and l % 2 == 0 and arr[i + k][j + l] == arr[i][j]
            ):  # 여기서 어차피 자기자리도 리버스 색칠됨
                ans2 += 1
            elif k % 2 == 1 and l % 2 == 1 and arr[i + k][j + l] == arr[i][j]:
                ans2 += 1
            elif k % 2 == 1 and l % 2 == 0 and arr[i + k][j + l] != arr[i][j]:
                ans2 += 1
            elif k % 2 == 0 and l % 2 == 1 and arr[i + k][j + l] != arr[i][j]:
                ans2 += 1
    if ans1 > ans2:
        return ans2
    else:
        return ans1


for i in range(N):
    arr.append(list(input()))
cnt = 2**31 - 1
for i in range(N - 7):
    for j in range(M - 7):
        if cnt > color(i, j):
            cnt = color(i, j)
print(cnt)
