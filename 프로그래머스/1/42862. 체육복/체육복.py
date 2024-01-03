def solution(n, lost, reserve):
    # 여벌 체육복을 가져온 학생 중 도난당한 학생 제외
    real_reserve = list(set(reserve) - set(lost))
    # 체육복을 도난당한 학생 중 여벌이 없는 학생 제외
    real_lost = list(set(lost) - set(reserve))
    
    for r in real_reserve:
        if r - 1 in real_lost:
            real_lost.remove(r - 1)
        elif r + 1 in real_lost:
            real_lost.remove(r + 1)
    
    answer = n - len(real_lost) # 체육복을 입을 수 있는 최대 학생 수
    return answer
