N = input()  # 분해합
num = int(N)
ans = 0

for i in range(num):
    arr_sum = i
    arr = str(i)
    for j in range(len(arr)):
        arr_sum += int(arr[j])
    if num == arr_sum:
        ans = i
        break

print(ans)
