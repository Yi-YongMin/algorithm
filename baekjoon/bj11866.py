N, K = map(int, input().split())
arr = [i + 1 for i in range(N)]
fin = 0
print("<", end="")
for i in range(N):
    fin += K - 1
    if fin >= len(arr):
        fin = fin % len(arr)
    if i < N - 1:
        print(f"{arr.pop(fin)},", end=" ")
    else:
        print(f"{arr.pop(fin)}", end="")
print(">")
