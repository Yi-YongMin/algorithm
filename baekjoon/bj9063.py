tc = int(input())
xpos = []
ypos = []
for i in range(tc):
    x, y = map(int, input().split())
    xpos.append(x)
    ypos.append(y)
print((max(xpos) - min(xpos)) * (max(ypos) - min(ypos)))
