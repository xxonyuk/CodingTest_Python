def solution(t, p):
    answer = 0
    t = list(t)
    for i in range(0, len(t)-len(p)+1):
        k = (''.join(t[i:i+len(p)]))
        if k <= p:
            answer +=1

    return answer