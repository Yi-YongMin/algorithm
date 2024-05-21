n = int(input())
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()
for p in range(n - 1):
    for k in range(p + 1):
        print(" ", end="")
    for k in range(2 * n - 3 - 2 * p):
        print("*", end="")
    print()
