def solution(arr):
    answer = []
    kk = min(arr)
    # if kk in arr:
    answer = arr.remove(kk)
    if len(arr) == 0:
        answer = [-1]
    else:
        answer = arr
    return answer