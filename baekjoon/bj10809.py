arr = input()
alphabet = [-1] * 26
for i in range(len(arr)):
    if alphabet[ord(arr[i]) - ord("a")] != -1:
        continue
    else:
        alphabet[ord(arr[i]) - ord("a")] = i
print(*alphabet)
