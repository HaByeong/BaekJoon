import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이 -> 내가 정석이다 야호!!
N, M = map(int, input().split())
numDict = dict()

for _ in range(N):
    word = input()
    if len(word) >= M and word not in numDict:
        numDict[word] = 0
    if len(word) >= M and word in numDict:
        numDict[word] += 1

numList = [
           [numDict[i], len(i), i] for i in numDict
           ]

# -> lambda x : () 기깔나게 썼다
numList.sort(key = lambda x : (-x[0], -x[1], x[2]))


for i in range(len(numList)):
    print(numList[i][2])