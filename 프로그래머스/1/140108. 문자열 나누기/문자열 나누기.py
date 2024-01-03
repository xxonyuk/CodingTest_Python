def solution(s):

    first =''
    samew = 0
    difw= 0
    answer = 0

    for i in s:
        if first == '':
            first = i
            samew = 1
            continue

        if first == i:
            samew += 1
        else:
            difw += 1

        if samew == difw:
            first = ''
            samew =0
            difw = 0
            answer += 1

    if first != '':
        answer +=1   
    return answer