import math


def solution(r1, r2):
    ans = 0
    for i in range(r2):
        b = int(math.sqrt(r2 * r2 - i * i))
        if i < r1:
            s = int(math.sqrt(r1 * r1 - i * i))
            ans += b - s
            if s == math.sqrt(r1 * r1 - i * i):
                print(s, math.sqrt(r1 * r1 - i * i))
                ans += 1

        else:
            ans += int(math.sqrt(r2 * r2 - i * i))
    return ans * 4


# def solution(r1, r2):
#     answer = 0
#     for i in range(1, r2 + 1):
#         if i < r1:
#             s = math.ceil(math.sqrt((r1**2 - i**2)))
#         else:
#             s = 0

#         e = int(math.sqrt((r2**2 - i**2)))
#         answer += e - s + 1

#     return answer * 4


print(solution(1, 2))
