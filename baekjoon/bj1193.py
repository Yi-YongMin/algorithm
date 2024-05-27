n = int(input())
row = [1]
col = [1]
start = 0
x, y = 0, 0
while True:
    if row[start] <= n <= col[start] or col[start] <= n <= row[start]:
        break
    start += 1
    if start % 2 == 1:
        row.append(row[start - 1] + 2 * start)
        col.append(col[start - 1] + 1)
    else:
        row.append(row[start - 1] + 1)
        col.append(col[start - 1] + 2 * start)
if n <= col[start]:
    k = col[start] - n
    a = 1 + k
    b = start + 1 - k
elif n <= row[start]:
    k = row[start] - n
    a = start + 1 - k
    b = 1 + k

print(str(a) + "/" + str(b), sep="")
