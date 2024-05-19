N = int(input())
sum = 0
iterator = N
for i in range(N):
    sum += iterator
    iterator -= 1
print(sum)
