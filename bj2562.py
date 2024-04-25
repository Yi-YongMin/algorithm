import sys

arr = []
maximum = 0
index = 0
for i in range(9):
    arr.append(int(sys.stdin.readline()))
    if maximum < arr[i]:
        maximum = arr[i]
        index = i + 1
print(maximum)
print(index)
