S = input()
ans = set()
tmp = len(S)
for i in range(tmp + 1):
    for j in range(tmp - i + 1):
        ans.add(S[j : j + i])
print(len(ans) - 1)

