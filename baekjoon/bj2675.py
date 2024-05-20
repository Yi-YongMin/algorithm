tc = int(input())
for i in range(tc):
    a, b = map(str, input().split())
    for k in range(len(b)):
        for j in range(int(a)):
            print(b[k], end="")
    print()
