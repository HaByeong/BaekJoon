import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

#나의 풀이
homesList = []
visited = []
deq = deque()
N = int(input())

#아파트 넣기
nList = [
    [0] + list(map(int, input()))
    for _ in range(N)
]
nList.insert(0, [0] * (N + 1))

#방문 체크
visited = [
    [0 for _ in range(N + 1)]
    for _ in range(N + 1)
]

#구현
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if nList[i][j] == 1 and visited[i][j] == 0:
            home_cnt = 0
            deq.append([i, j])
            visited[i][j] = 1
            while deq:
                home_cnt += 1
                popList = deq.popleft()
                x, y = popList[0], popList[1]
                if (x - 1) > 0 and nList[x - 1][y] == 1 and visited[x - 1][y] == 0:
                    deq.append([x - 1, y])
                    visited[x - 1][y] = 1
                if (y - 1) > 0 and nList[x][y -1] == 1 and visited[x][y - 1] == 0:
                    deq.append([x, y - 1])
                    visited[x][y - 1] = 1
                if x + 1 <= N and nList[x + 1][y] == 1 and visited[x + 1][y] == 0:
                    deq.append([x + 1, y])
                    visited[x + 1][y] = 1
                if y + 1 <= N and nList[x][y + 1] == 1 and visited[x][y + 1] == 0:
                    deq.append([x, y + 1])
                    visited[x][y + 1] = 1
            homesList.append(home_cnt)

print(len(homesList))
for i in sorted(homesList):
    print(i)






