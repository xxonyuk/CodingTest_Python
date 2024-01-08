def solution(n):
    answer = 0
    x = bin(n).count('1')
    while True:
        n += 1
        if bin(n).count('1') == x:
            break
    return n