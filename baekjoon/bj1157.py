arr = input()
ans = {}
start = 1

for i in range(len(arr)):
    if arr[i].upper() not in ans.keys():
        ans[arr[i].upper()] = start
    else:
        ans[arr[i].upper()] += 1

max_key = [k for k, value in ans.items() if max(ans.values()) == value]

prt = max(ans, key=ans.__getitem__)
if len(max_key) > 1:
    prt = "?"

print(prt)
