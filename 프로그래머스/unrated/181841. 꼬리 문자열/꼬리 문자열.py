def solution(str_list, ex):
    aa = []
    for i in str_list:
        if not ex in i:
            aa.append(i)
    answer = ''.join(aa)
    return answer