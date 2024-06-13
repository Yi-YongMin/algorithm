# def solution(length, weight, truck_weights):
#     bridge = [[1], [truck_weights.pop(0)]]
#     answer = 1
#     while True:
#         answer += 1
#         if len(bridge[0]) == 0:
#             print(answer)
#             break
#         for i in range(len(bridge[0])):
#             bridge[0][i] += 1
#         if bridge[0][0] == length + 1:
#             bridge[0].pop(0)
#             bridge[1].pop(0)
#         if len(truck_weights) != 0 and sum(bridge[1]) + truck_weights[0] <= weight:
#             bridge[1].append(truck_weights.pop(0))
#             bridge[0].append(1)
#     return answer - 1

from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    time = 0
    current_weight = 0

    while bridge:
        time += 1
        current_weight -= bridge.popleft()

        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                current_weight += truck
            else:
                bridge.append(0)

    return time
