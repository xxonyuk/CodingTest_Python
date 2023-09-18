def solution(s):
    answer = sorted(s, reverse=True)
    k = ''.join(answer)
    return k