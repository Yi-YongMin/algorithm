N = int(input())
cnt = 2


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


# 자기가 소수인경우...?
while N != 1:
    if N % cnt == 0:
        print(cnt)
        N = N // cnt
    else:
        cnt += 1
