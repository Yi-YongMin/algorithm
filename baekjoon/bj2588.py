a = int(input())
b = int(input())
num1 = (b % 10) * a
num2 = (b % 100) // 10 * a
num3 = b // 100 * a
print(num1)
print(num2)
print(num3)
print(a * b)
