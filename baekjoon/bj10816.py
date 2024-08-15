N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))
s2 = {}
for i in arr1:
    if i in s2:
        s2[i] += 1
    else:
        s2[i] = 1
for i in arr2:
    if i in s2:
        print(s2[i], end=" ")
    else:
        print(0, end=" ")
