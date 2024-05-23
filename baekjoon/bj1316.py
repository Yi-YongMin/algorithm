def checker(word):
    cnt = 1
    check = set()
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            cnt += 1
            check.add(word[i])
    check.add(word[len(word) - 1])
    ans = int(1) if len(check) == cnt else int(0)
    return ans


N = int(input())
ans = 0
for j in range(N):
    arr = input()
    ans += checker(arr)
print(ans)
