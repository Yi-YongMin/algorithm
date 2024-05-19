a, b, c = map(int, input().split())
if a == b == c:
    print(str(10000 + a * 1000))
elif a == b:
    print(str(1000 + a * 100))
elif b == c:
    print(str(1000 + b * 100))
elif a == c:
    print(str(1000 + a * 100))
else:
    tmp = a
    for i in range(2):
        if tmp < b:
            tmp = b
        elif tmp < c:
            tmp = c
    print(str(tmp * 100))
