N, M = map(int, input().split())
dd = set()
dbd = []
cnt = 0
for i in range(N):
    a = input()
    dd.add(a)
for i in range(M):
    a = input()
    if a in dd:
        cnt += 1
        dbd.append(a)
dbd.sort()
print(cnt)
for i in range(cnt):
    print(dbd[i])
