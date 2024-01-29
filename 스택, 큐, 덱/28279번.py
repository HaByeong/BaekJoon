import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

#나의 풀이
def deque_fuction(x):
    userInput = list(map(int, x.split()))
    if userInput[0] == 1:
        Deque.appendleft(userInput[1])
    elif userInput[0] == 2:
        Deque.append(userInput[1])
    elif userInput[0] == 3:
        print(Deque.popleft() if Deque else -1)
    elif userInput[0] == 4:
        print(Deque.pop() if Deque else -1)
    elif userInput[0] == 5:
        print(len(Deque))
    elif userInput[0] == 6:
        print(0 if Deque else 1)
    elif userInput[0] == 7:
        print(Deque[0] if Deque else -1)
    elif userInput[0] == 8:
        print(Deque[-1] if Deque else -1)

Deque = deque()
N = int(input())

for _ in range(N):
    userInput = input()
    deque_fuction(userInput)
