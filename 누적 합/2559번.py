import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N, K = map(int, input().split())
numList = list(map(int, input().split()))
sumList = [0] * N
ansList = []

for i in range(N):
    if i == 0:
        sumList[0] = numList[0]
    else:
        sumList[i] = sumList[i - 1] + numList[i]

for i in range(K - 1, N):
    if i == (K - 1):
        ansList.append(sumList[i])
    else:
        ansList.append(sumList[i] - sumList[i - K])
print(max(ansList))



