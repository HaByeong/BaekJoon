import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

#나의 풀이
def queue(x):
    while len(x) > 1:
        x.popleft()
        x.append(x.popleft())
    print(x[0])

N = int(input())
Queue = [
    i for i in range(1, N + 1)
]

queue(deque(Queue))

#정석 풀이 -> rotate 사용(양수면 오른쪽으로 돌고, 음수면 왼쪽으로 돈다)
def queue(x):
    while len(x) > 1:
        x.popleft()
        x.rotate(-1)
    print(x[0])

N = int(input())
Queue = deque(range(1, N + 1))

queue(Queue)
