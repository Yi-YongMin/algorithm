arr = input()
ans = 0
for i in range(len(arr)):
    if ord(arr[i]) < 80:
        ans = ans + 3 + (ord(arr[i]) - 65) // 3
    else:
        if arr[i] in "PQRS":
            ans = ans + 6 + 2
        elif arr[i] in "TUV":
            ans = ans + 7 + 2
        else:
            ans += 10
print(ans)
