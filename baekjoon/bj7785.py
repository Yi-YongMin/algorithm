N = int(input())
ans = set()
for i in range(N):
    a, b = map(str, input().split())
    if b == "enter":
        ans.add(a)
    elif b == "leave":
        ans.remove(a)
p = sorted(list(ans), reverse=True)
for i in range(len(p)):
    print(p[i])
