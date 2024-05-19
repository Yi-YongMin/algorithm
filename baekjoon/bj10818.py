import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
minimun = arr[0]
maximum = arr[0]
for i in range(N):
    if minimun > arr[i]:
        minimun = arr[i]
    if maximum < arr[i]:
        maximum = arr[i]
print(minimun, maximum)
