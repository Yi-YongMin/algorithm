def solution(arr):
    answer = []
    n = len(arr)
    answer.append(arr[0])
    for i in range(1, n):
        if arr[i - 1] != arr[i]:
            answer.append(arr[i])
    return answer


arr = [4, 4, 4, 3, 3]
print(solution(arr))
