K = int(input())
arr = []
for i in range(K):
    a = int(input())
    if a == 0:
        arr.pop()
    else:
        arr.append(a)
print(sum(arr))
