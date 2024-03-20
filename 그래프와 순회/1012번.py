import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque
#나의 풀이
deq = deque()
T = int(input())


for _ in range(T):
    M, N, K = map(int, input().split())
    cnt = 0

    #배추 밭이랑 visited 만들기
    nList = [
        [0] * N
        for _ in range(M)
    ]
    visited = [
        [0] * N
        for _ in range(M)
    ]
    for _ in range(K):
        X, Y = map(int, input().split(" "))
        nList[X][Y] = 1

    #구현
    for i in range(M):
        for j in range(N):
            if nList[i][j] == 1 and visited[i][j] == 0:
                deq.append([i, j])
                visited[i][j] = 1
                while deq:
                    popList = deq.popleft()
                    x, y = popList[0], popList[1]
                    if (x - 1 >= 0) and nList[x - 1][y] == 1 and visited[x - 1][y] == 0:
                        deq.append([x - 1, y])
                        visited[x - 1][y] = 1
                    if (y - 1 >= 0) and nList[x][y - 1] == 1 and visited[x][y - 1] == 0:
                        deq.append([x, y - 1])
                        visited[x][y - 1] = 1
                    if (x + 1 < M) and nList[x + 1][y] == 1 and visited[x + 1][y] == 0:
                        deq.append([x + 1, y])
                        visited[x + 1][y] = 1
                    if (y + 1 < N) and nList[x][y + 1] == 1 and visited[x][y + 1] == 0:
                        deq.append([x, y + 1])
                        visited[x][y + 1] = 1
                cnt += 1
    print(cnt)



