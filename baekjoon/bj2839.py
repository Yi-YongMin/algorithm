N = int(input())
ans = N
cnt = -1
a5, a3 = 0, N // 3
while 1:
    a3 = N // 3
    if a3 < 0:
        break
    if (a5 * 5 + a3 * 3) == ans:
        cnt = a5 + a3
        # print("후보군 a5 : ", a5, " a3 : ", a3)
    # print("a5 : ", a5, " a3 : ", a3, " N : ", N)
    a5 += 1
    N -= 5
print(cnt)
