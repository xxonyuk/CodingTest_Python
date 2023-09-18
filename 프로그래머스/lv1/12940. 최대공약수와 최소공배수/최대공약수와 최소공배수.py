def solution(x, y):
    answer = []
    a= 0
    b=0
    for i in range(min(x,y),0,-1):
        if x % i == 0 and y % i == 0:
            a = i
            break
    answer.append(a)
    for i in range(max(x,y),(x*y)+1):
        if i % x == 0 and i % y ==0:
            b = i
            break
    answer.append(b)
    return answer