import itertools

def PrimeNum(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def solution(nums):
    s = 0
    answer = 0
    nums.sort()
    nn = list(itertools.combinations(nums,3))
    for i in nn:
        s = sum(i)
        if PrimeNum(s) == True:
            answer +=1
    return answer