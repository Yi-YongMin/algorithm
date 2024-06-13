def solution(answers):
    answer = []
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1, cnt2, cnt3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == arr1[i % 5]:
            cnt1 += 1
        if answers[i] == arr2[i % 8]:
            cnt2 += 1
        if answers[i] == arr3[i % 10]:
            cnt3 += 1
    ans = max(cnt1, cnt2, cnt3)
    if cnt1 == ans:
        answer.append(1)
    if cnt2 == ans:
        answer.append(2)
    if cnt3 == ans:
        answer.append(3)
    return answer
