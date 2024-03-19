import sys
from collections import deque
#sys.setrecursionlimit(10 ** 7)
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N, M, V = map(int, input().split())
dfs_visited = [0] * (N + 1)
bfs_visited = [0] * (N + 1)
nearNode = [[] for _ in range(N + 1)]
deq = deque()

for _ in range(M):
    u, v = map(int, input().split())
    nearNode[u].append(v)
    nearNode[v].append(u)

#DFS
def dfs(num):
    if dfs_visited[num] != 0:
        return
    print(num, end = " ")
    dfs_visited[num] = 1
    sortList = sorted(nearNode[num])
    for i in sortList:
        if dfs_visited[i] == 0:
            dfs(i)
dfs(V)

#띄어쓰기
print()

#BFS
deq.append(V)
bfs_visited[V] = 1

while deq:
    popValue = deq.popleft()
    print(popValue, end = " ")
    sortList = sorted(nearNode[popValue])
    for i in sortList:
        if bfs_visited[i] == 0:
            deq.append(i)
            bfs_visited[i] = 1



