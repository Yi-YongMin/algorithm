a, b, top = map(int, input().split())
today = a - b
cand = top / today
cnt = round(cand)
standard = (top - a) / today + 1
while True:
    if cnt < standard:
        break
    cnt -= 1

print(cnt + 1)
