def solution(s): 
    answer = []
    last_seen = {}
    
    for i, char in enumerate(s):
        if char not in last_seen:
            last_seen[char] = i
            answer.append(-1)
            
        else:
            prev = last_seen[char]
            answer.append(i - prev)
            last_seen[char] = i

    return answer
