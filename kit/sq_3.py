def solution(s):
    cnt = 0
    for i in range(len(s)):
        if cnt < 0:
            return False
        elif s[i] == "(":
            cnt += 1
        elif s[i] == ")":
            cnt -= 1
    if cnt == 0:
        return True
    else:
        return False
