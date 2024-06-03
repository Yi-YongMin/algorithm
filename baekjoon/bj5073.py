while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    elif a == b == c:
        print("Equilateral")
    elif a >= b + c or b >= a + c or c >= a + b:
        print("Invalid")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
