H, M = map(int, input().split())
if M >= 45:
    print(str(H) + " " + str(M - 45))
elif H == 0 and M < 45:
    print("23 " + str(60 + M - 45))
else:
    print(str(H - 1) + " " + str(60 + M - 45))
