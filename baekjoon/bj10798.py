arr = [[] for _ in range(5)]
len_list = []

for i in range(5):
    arr[i] = input()
    len_list.append(len(arr[i]))
max_len = max(len_list)
ans_list = []
for i in range(max_len):
    for j in range(5):
        if len(arr[j]) < i + 1:
            pass
        else:
            ans_list.append(arr[j][i])
print(*ans_list, sep="")
