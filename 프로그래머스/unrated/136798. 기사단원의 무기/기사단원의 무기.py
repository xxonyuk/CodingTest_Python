def AA(n):
    a = 0
    if int(n**0.5) == n **0.5: # 제곱수
        for i in range(1, int(n**0.5)+1):
            if n % i ==0:
                a += 1
        return a * 2 -1
    else:
        for i in range(1, int(n**0.5)+1):
            if n % i ==0:
                a += 1
        return a * 2

def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        if AA(i) <= limit:
            answer += AA(i)
        else:
            answer += power

    return answer