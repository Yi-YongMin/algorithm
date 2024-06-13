def solution(sizes):
    answer = 0
    wi, he = 0, 0
    for w, h in sizes:
        if w > wi or h > he:
            if abs(w - wi) + abs(he - h) < abs(w - he) + abs(h - wi):
                wi = max(w, wi)
                he = max(he, h)
            else:
                wi = max(wi, h)
                he = max(he, w)
    answer = wi * he
    return answer


# 이거말고도 큰것중에 가장 큰것 * 작은것 중에 가장 큰것 도 가능
