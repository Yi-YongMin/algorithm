arr = []
for i in range(3):
    a = int(input())
    arr.append(a)
if sum(arr) != 180:
    print("Error")
else:
    if arr[0] == arr[1] == arr[2]:
        print("Equilateral")
    elif arr[0] == arr[1] or arr[1] == arr[2] or arr[0] == arr[2]:
        print("Isosceles")
    else:
        print("Scalene")
