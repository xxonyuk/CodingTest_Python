import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    for j in range(2, n+1):
        if isPrime(j) == True:

            answer += 1
                       
    return answer