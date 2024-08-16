N, M = map(int, input().split())
d1 = {}
d2 = {}
for i in range(1, N + 1):
    a = input()
    d1[i] = a
    d2[a] = i
for i in range(M):
    b = input()
    if b.isdigit():
        print(d1[int(b)])
    else:
        print(d2[b])
