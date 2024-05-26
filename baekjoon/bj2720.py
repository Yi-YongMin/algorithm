T = int(input())
ls = [25, 10, 5, 1]
for i in range(T):
    money = int(input())
    ans = []
    ans.append(money // ls[0])
    money = money % ls[0]
    ans.append(money // ls[1])
    money = money % ls[1]
    ans.append(money // ls[2])
    money = money % ls[2]
    ans.append(money // ls[3])
    print(*ans)
