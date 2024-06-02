xpos = []
ypos = []
x, y = 0, 0
for i in range(3):
    a, b = map(int, input().split())
    xpos.append(a)
    ypos.append(b)
if xpos[0] == xpos[1]:
    x = xpos[2]
elif xpos[1] == xpos[2]:
    x = xpos[0]
elif xpos[0] == xpos[2]:
    x = xpos[1]
if ypos[0] == ypos[1]:
    y = ypos[2]
elif ypos[1] == ypos[2]:
    y = ypos[0]
elif ypos[0] == ypos[2]:
    y = ypos[1]

print(x, y)
