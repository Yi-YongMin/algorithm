N, cut = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
print(arr[cut - 1])
print(arr)
