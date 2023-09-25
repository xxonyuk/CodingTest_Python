def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        k = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(k[commands[i][-1]-1])
    return answer