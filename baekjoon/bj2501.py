a, b = map(int, input().split())
cnt = 1
arr = []
while cnt <= a / 2:
    if a % cnt == 0:
        arr.append(cnt)
    cnt += 1
arr.append(a)
if len(arr) < b:
    print(0)
else:
    print(arr[b - 1])
