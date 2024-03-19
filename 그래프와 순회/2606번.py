import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

#나의 풀이
N = int(input()) # 컴퓨터의 수
M = int(input()) # 연결되어 있는 컴퓨터 쌍의 수
nearNode = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
cnt = 0
deq = deque()

deq.append(1)
visited[1] = 1

for _ in range(M):
    a, b = map(int, input().split())
    nearNode[a].append(b)
    nearNode[b].append(a)

while deq:
    popValue = deq.popleft()
    for i in nearNode[popValue]:
        if visited[i] == 0:
            cnt += 1
            deq.append(i)
            visited[i] = 1

print(cnt)
