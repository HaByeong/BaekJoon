import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

#나의 풀이 -> 내가 정석
N, K = map(int, input().split())

Queue = deque(range(1, N + 1))

print("<", end = "")
while len(Queue) > 0:
    Queue.rotate(K * -1)
    print(Queue.pop(), end = "")
    if len(Queue) != 0:
        print(", ", end = "")
    else:
        print(">", end = "")

