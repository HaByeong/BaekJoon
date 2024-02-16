import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이 -> 백트레킹할 때 모든 경우의 수를 탐색하지말자... 흑흑
def DFS(index, num):
    global minValue
    if index == end:
        tSum, fSum = 0, 0
        for i in range(N):
            for j in range(N):
                if checkList[i] and checkList[j]:
                    tSum += numList[i][j]
                elif not checkList[i] and not checkList[j]:
                    fSum += numList[i][j]
        value = fSum - tSum
        if value >= 0 and minValue > value:
            minValue = value
        return
    for i in range(num, N):
        if checkList[i] == False:
            checkList[i] = True
            DFS(index + 1, i + 1)
            checkList[i] = False

N = int(input())
end = N // 2
numList = [
    list(map(int, input().split()))
    for _ in range(N)
]
checkList = [False] * N
minValue = 2999999
DFS(0, 0)
print(minValue)