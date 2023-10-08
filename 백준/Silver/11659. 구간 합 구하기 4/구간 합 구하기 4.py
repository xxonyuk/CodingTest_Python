import sys
input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int,input().split()))

t = 0
sl = [0]
for i in numbers:
    t += i
    sl.append(t)
    
for i in range(quizNo):
    a, b = map(int, input().split())
    print(sl[b]-sl[a-1])