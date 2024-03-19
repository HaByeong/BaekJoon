import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

#나의 풀이
max = 100000
N, M, R = map(int, input().split())
visit = [0] * (N + 1)
list = [[] for _ in range(max + 1)]
deq = deque()
cnt = 1

for _ in range(M):
    u, v = map(int, input().split())
    list[u].append(v)
    list[v].append(u)

deq.append(R)
visit[R] = cnt
while True:
    if len(deq) == 0:
        break
    popValue = deq.popleft()
    for i in sorted(list[popValue]):
        if visit[i] == 0:
            cnt += 1
            deq.append(i)
            visit[i] = cnt

for i in visit[1:]:
    print(i)

#코드 개선
max = 100000
N, M, R = map(int, input().split())
visit = [0] * (N + 1)
list = [[] for _ in range(max + 1)]
deq = deque()
cnt = 1

for _ in range(M):
    u, v = map(int, input().split())
    list[u].append(v)
    list[v].append(u)

deq.append(R)
visit[R] = cnt
while deq:
    popValue = deq.popleft()
    for i in sorted(list[popValue]):
        if visit[i] == 0:
            cnt += 1
            deq.append(i)
            visit[i] = cnt

for i in visit[1:]:
    print(i)
