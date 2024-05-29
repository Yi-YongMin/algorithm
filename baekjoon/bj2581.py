a = int(input())
b = int(input())


def prime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


arr = []
for i in range(a, b + 1):
    if prime(i) == True:
        arr.append(i)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])
