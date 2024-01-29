import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

#나의 풀이 -> 삼항 연산자쓰면 연산시간 좀 더 걸린다
Queue = deque()
def queue(x):
    userInput = list(x.split())
    if userInput[0] == "push":
        Queue.append(userInput[1])
    elif userInput[0] == "pop":
        print(Queue.popleft() if Queue else -1)
    elif userInput[0] == "size":
        print(len(Queue))
    elif userInput[0] == "front":
        print(Queue[0] if Queue else -1)
    elif userInput[0] == "back":
        print(Queue[-1] if Queue else -1)
    elif userInput[0] == "empty":
        print(0 if Queue else 1)

N = int(input())

for _ in range(N):
    x = input()
    queue(x)

#정석 풀이



