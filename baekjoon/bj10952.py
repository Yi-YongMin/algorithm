A, B = 1, 1
while A != 0 or B != 0:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        exit()
    print(A + B)
