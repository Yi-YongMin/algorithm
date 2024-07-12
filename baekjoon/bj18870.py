N = int(input())
arr = list(map(int, input().split()))


arr1 = sorted(set(arr))
# print(arr1)
dic = {val: idx for idx, val in enumerate(arr1)}
# print(dic)

ans = [dic[val] for val in arr]  # 동일한 value라면 같은 idx를 가진다.
# print(ans)
print(" ".join(map(str, ans)))
