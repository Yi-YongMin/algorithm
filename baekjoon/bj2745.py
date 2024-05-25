N, B = input().split()
zin = int(B)
ans = 0
num = len(N)
for i in range(num):  # 역순
    now = num - i - 1
    if ord(N[now]) <= 57:
        ans += int(N[now]) * (zin**i)
    elif ord(N[now]) >= 65:
        ans += (ord(N[now]) - 65 + 10) * (zin**i)

print(ans)
