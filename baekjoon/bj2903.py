# 2 3 5 9 17 33
T = int(input())
start = 2
for i in range(T):
    start += 2**i
print(start * start)
