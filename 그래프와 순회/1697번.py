import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

#나의 풀이
Max = 100000
N, K = map(int, input().split())
dist = [0] * (Max + 1)

q = deque()
q.append(N)

while q:
    x = q.popleft()
    if x == K:
        print(dist[K])
        break
    for i in (x - 1, x + 1, x * 2):
        if (0 <= i <= Max) and dist[i] == 0:
            q.append(i)
            dist[i] = dist[x] + 1





