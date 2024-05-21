arr = input()
ans = 1
for i in range(len(arr) // 2):
    if arr[i] != arr[len(arr) - i - 1]:
        ans = 0
        break
print(ans)
