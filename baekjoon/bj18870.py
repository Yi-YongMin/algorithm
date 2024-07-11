N = int(input())
arr = list(map(int, input().split()))
arr1 = []
for i in range(N):
    arr1.append([arr[i], i])
arr1.sort(key=lambda x: (x[0]))  # 원본 값,원본 인덱스에서 원본 값을 기준으로 정렬
idx = 0
ans = []
for i in range(N - 1):
    if arr1[i][0] == arr1[i + 1][0]:
        ans.append([idx, arr1[i][1]])
    else:
        ans.append([idx, arr1[i][1]])
        idx += 1

if arr1[N - 2][0] == arr1[N - 1][0]:
    ans.append([idx, arr1[N - 1][1]])
else:
    idx += 1
    ans.append([idx, arr1[N - 1][1]])

# for i in range(N):
#     print(ans[i], end=" ")
ans.sort(key=lambda x: (x[1]))

for i in range(N):
    print(ans[i][0], end=" ")
