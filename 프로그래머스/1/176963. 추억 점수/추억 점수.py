def solution(name, yearning, photo):
    answer = []
    new = dict(zip(name, yearning))
    for i in photo:
        a= 0
        for j in i:
            if j in name:
                a += new[j]
            else:
                a += 0
        answer.append(a)

    return answer