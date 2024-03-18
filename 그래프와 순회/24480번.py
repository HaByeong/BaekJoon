import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 6)

#나의 풀이
def dfs(R):
    global cnt
    if V[R] != 0:
        return
    cnt += 1
    V[R] = cnt
    E[R].sort(reverse = True)
    for i in E[R]:
        if V[i] == 0:
            dfs(i)

N, M, R = map(int, input().split())
cnt = 0
V = [0] * (N + 1)
E = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

dfs(R)

for i in V[1:]:
    print(i)

