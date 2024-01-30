import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

#나의 풀이 -> deque는 생각해보면 결국 원이다!
N = int(input())
numIn = list(map(int, input().split()))
Deque = deque(range(1, N + 1))

#처음에 1은 따로 처리해주자(디폴트로 첫 시작이니)
bombNum = Deque.popleft()
print(bombNum, end = " ")

while len(Deque) > 0:
    moveNum = numIn[bombNum - 1]
    if len(Deque) == 1:
        print(Deque.pop())
        break
    if moveNum > 0:
        Deque.rotate(moveNum * -1)
        bombNum = Deque.pop()
    else:
        Deque.rotate(moveNum * -1)
        bombNum = Deque.popleft()
    print(bombNum, end=" ")

#정석 풀이 -> enumerate 사용
N = int(input())
Q = deque(enumerate(map(int, input().split())))
ans = []

while Q:
    idx, paper = Q.popleft()
    ans.append(idx + 1)

    if paper > 0:
        Q.rotate(-(paper - 1))
    elif paper < 0:
        Q.rotate(-paper)
print(' '.join(map(str, ans)))





