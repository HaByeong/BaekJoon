import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

#나의 풀이
deq = deque()
M, N = map(int, input().split())
tomato = [
    list(map(int, input().split()))
    for _ in range(N)
]

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            deq.append([i, j])

while deq:
    popList = deq.popleft()
    x, y = popList[0], popList[1]
    if (x - 1) >= 0 and tomato[x - 1][y] == 0:
        deq.append([x - 1, y])
        tomato[x - 1][y] = tomato[x][y] + 1
    if (x + 1) < N and tomato[x + 1][y] == 0:
        deq.append([x + 1, y])
        tomato[x + 1][y] = tomato[x][y] + 1
    if (y - 1) >= 0 and tomato[x][y - 1] == 0:
        deq.append([x, y - 1])
        tomato[x][y - 1] = tomato[x][y] + 1
    if (y + 1) < M and tomato[x][y + 1] == 0:
        deq.append([x, y + 1])
        tomato[x][y + 1] = tomato[x][y] + 1

check = 0
max = tomato[0][0]
for i in tomato:
    for j in i:
        if j == 0:
            check = 1
        if max < j:
            max = j
if check == 0:
    print(max - 1)
else:
    print(-1)
