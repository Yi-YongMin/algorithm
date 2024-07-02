arr = input()
ans = []
for i in range(len(arr)):
    ans.append(int(arr[i]))
ans.sort(reverse=True)
print(*ans, sep="")
