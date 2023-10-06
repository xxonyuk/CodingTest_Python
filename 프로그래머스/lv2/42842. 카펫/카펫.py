def solution(brown, yellow):
    answer = []

    a, b, k = 0, 0,0
    # BW + BH = a 
    # BW * BH = b
    a = (brown + 4)//2
    b = brown + yellow
    

    k = (a** 2 - 4*b) ** 0.5  # BW-BH
    answer.append(int((a + k)//2))
    answer.append(int((a - k)//2 ))
    
    return answer