import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque
#나의 풀이
max = 100000
N, M, R = map(int, input().split())
visit = [0] * (N + 1)
nearNode = [[] for _ in range(N + 1)]
cnt = 1
deq = deque()

for _ in range(M):
    u, v = map(int, input().split())
    nearNode[u].append(v)
    nearNode[v].append(u)

visit[R] = cnt
deq.append(R)

while deq:
    popValue = deq.popleft()
    nlist = sorted(nearNode[popValue], reverse = True)
    for i in nlist:
        if visit[i] == 0:
            deq.append(i)
            cnt += 1
            visit[i] = cnt

for i in visit[1:]:
    print(i)
