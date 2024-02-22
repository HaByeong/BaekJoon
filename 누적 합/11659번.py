import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N, M = map(int, input().split())
numList = list(map(int, input().split()))
ansList = [0] * N

for i in range(N):
    ansList[i] = ansList[i - 1] + numList[i]

for i in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(ansList[j - 1])
    elif i == N:
        print(numList[i - 1])
    else:
        print(ansList[j - 1] - ansList[i - 2])



