import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)
#나의 풀이
#V: 정점 집합, E: 간선 집합, R: 시작 정점
def dfs (R):
    global cnt
    if visited[R] != 0:
        return
    cnt += 1
    visited[R] = cnt
    if R in E:
        if len(E[R]) > 1:
            E[R].sort()
        for i in E[R]:
            if visited[i] == 0:
                dfs(i)
    else:
        return
N, M, R = map(int, input().split())
visited = [0] * (N + 1)
E = dict()
cnt = 0

for i in range(M):
    u, v = map(int, input().split())
    if u not in E:
        E[u] = []
    if v not in E:
        E[v] = []
    E[u].append(v)
    E[v].append(u)

dfs(R)

for i in visited[1:]:
    print(i)

#정석 풀이 -> dict 말고 그냥 리스트로 나타내보자
N, M, R = map(int, input().split())
visited = [0] * (N + 1)
E = [[] for _ in range(N + 1)]
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

def dfs (R):
    global cnt
    if visited[R] != 0:
        return
    cnt += 1
    visited[R] = cnt

    E[R].sort()
    for i in E[R]:
        if visited[i] == 0:
            dfs(i)

dfs(R)

for i in visited[1:]:
    print(i)
