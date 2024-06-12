def solution(length, weight, truck_weights):
    bridge = [[1], [truck_weights.pop(0)]]
    answer = 1
    while True:
        answer += 1
        if len(bridge[0]) == 0:
            print(answer)
            break
        for i in range(len(bridge[0])):
            bridge[0][i] += 1
        if bridge[0][0] == length + 1:
            bridge[0].pop(0)
            bridge[1].pop(0)
        if len(truck_weights) != 0 and sum(bridge[1]) + truck_weights[0] <= weight:
            bridge[1].append(truck_weights.pop(0))
            bridge[0].append(1)
    return answer - 1
