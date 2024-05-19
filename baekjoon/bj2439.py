N = int(input())
for i in range(N):
    for t in range(1, N - i):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end="")
    print("")
