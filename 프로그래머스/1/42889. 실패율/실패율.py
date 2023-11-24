def solution(N, stages):
    answer =[]
    
    ratio ={}
    allplayer = len(stages)
    for i in range(1, N+1):
        if allplayer == 0:
            ratio[i] = 0
        else:
            ratio[i] = stages.count(i)/allplayer
            allplayer -= stages.count(i)
    answer = sorted(ratio, key=lambda x : ratio[x], reverse=True)
    return answer