import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = int(input())
queueStack = tuple(input().split())
queueStackNum = list(input().split())

M = int(input())
numIn = tuple(input().split())

for i in range(M):
    num = numIn[i]
    for j in range(N):
        if queueStack[j] == '0':
            num2 = queueStackNum[j]
            queueStackNum[j] = num
            num = num2
    print(num, end = " ")



