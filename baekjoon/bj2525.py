H, M = map(int, input().split())
C = int(input())
sh = C // 60
sm = C % 60

if M + sm >= 60:
    if H + sh >= 23:
        print(str(H + sh - 23) + " " + str(M + sm - 60))
    else:
        print(str(H + sh + 1) + " " + str(M + sm - 60))
else:
    if H + sh >= 24:
        print(str(H + sh - 24) + " " + str(M + sm))
    else:
        print(str(H + sh) + " " + str(M + sm))
