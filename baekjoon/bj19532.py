a, b, c, d, e, f = map(int, input().split())
ans1, ans2 = -1000, -1000
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            ans1 = x
            ans2 = y
            break
    if ans1 != -1000:
        break
print(ans1, ans2)
