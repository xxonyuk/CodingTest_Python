from collections import deque
def solution(s):
    answer = True
    deq = deque(s)
        
    cnt1 , cnt2 = 0, 0
    while len(deq):
        if deq.popleft() == '(':
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt2 > cnt1:
            answer = False
            break
    if cnt1 == cnt2:
        answer = True
    else:
        answer = False

        
    return answer