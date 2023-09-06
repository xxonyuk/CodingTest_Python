def solution(s):
    answer = ''
    kk = ''

    kk = list(map(int, s.split()))

    s = min(kk)
    # print(s)
    a = max(kk)
    answer += str(s)
    answer += ' '
    answer += str(a)
    return answer