import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
highest = max(arr)
print(sum(arr) / highest * 100 / len(arr))
