import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

#나의 풀이1
max = 10000
sList = (max + 1) * [0]
check = (max + 1) * [0]
deq = deque()
S, E = map(int, input().split())
deq.append(S)
check[S] = 1
sList[S] = 0

while True:
    x = deq.popleft()
    if x == E:
        break
    for i in (x - 1, x + 1, x + 5):
        if check[i] != 0:
            continue
        sList[i] = sList[x] + 1
        check[i] = 1
        deq.append(i)
print(sList[E])
