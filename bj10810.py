import sys

N, M = map(int, sys.stdin.readline().split())
basket = [0] * (N + 1)
for l in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for index in range(i, j + 1):
        basket[index] = k

print(*basket[1 : N + 1])
