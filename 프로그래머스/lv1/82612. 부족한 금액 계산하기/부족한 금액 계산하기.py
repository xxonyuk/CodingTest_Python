def solution(price, money, count):
    a = 0
    for i in range(1, count+1):
        a += price * i 
    
    if a-money <= 0:
        answer = 0
    else:
        answer = a-money
    return answer