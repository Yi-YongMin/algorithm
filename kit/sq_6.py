from collections import deque


def solution(prices):
    answer = []
    length = len(prices)
    cnt = 0
    for i in range(length):
        now = prices[i]
        cnt += 1
        if cnt == length:
            answer.append(0)
            break
        for j in range(i, length):
            if now > prices[j]:
                answer.append(j - i)
                break
            elif j == length - 1:
                answer.append(length - i - 1)

    return answer


def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

    for i in range(n):
        # 스택의 최상단 원소보다 현재 가격이 떨어지면 스택에서 pop
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    # 스택에 남아있는 원소들의 처리
    while stack:
        j = stack.pop()
        answer[j] = n - j - 1

    return answer
