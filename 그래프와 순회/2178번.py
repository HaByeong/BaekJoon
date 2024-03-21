import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

#나의 풀이
N, M = map(int, input().split())
deq = deque()

#미로 만들기
miro = [
    list(map(int,input()))
    for _ in range(N)
]

#순서 넣는 리스트
cntList = [
    [0] * M
    for _ in range(N)
]

#구현
#시작 지점 세팅
deq.append([0, 0])
cntList[0][0] = 1

while deq:
    popList = deq.popleft()
    x, y = popList[0], popList[1]
    if (x + 1) < N and miro[x + 1][y] == 1 and cntList[x + 1][y] == 0:
        deq.append([x + 1, y])
        cntList[x + 1][y] = cntList[x][y] + 1
    if (x - 1) >= 0 and miro[x - 1][y] == 1 and cntList[x - 1][y] == 0:
        deq.append([x - 1, y])
        cntList[x - 1][y] = cntList[x][y] + 1
    if (y + 1) < M and miro[x][y + 1] == 1 and cntList[x][y + 1] == 0:
        deq.append([x, y + 1])
        cntList[x][y + 1] = cntList[x][y] + 1
    if (y - 1) >= 0 and miro[x][y - 1] == 1 and cntList[x][y - 1] == 0:
        deq.append([x, y - 1])
        cntList[x][y - 1] = cntList[x][y] + 1
for i in cntList:
    for j in i:
        print(j, end = "")
    print()
