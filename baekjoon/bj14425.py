N, M = map(int, input().split())
s = set()
cnt = 0
for i in range(N):
    s.add(input())
for i in range(M):
    ans = input()
    if ans in s:
        cnt += 1
print(cnt)
