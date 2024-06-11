a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
f = a1 * n0 + a0
if a1 <= c and f <= c * n0:
    print(1)
else:
    print(0)
