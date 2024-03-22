import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

#나의 풀이
N = int(input())

for _ in range(N):
    deq = deque()
    I = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    #체스판 방문 확인 리스트 만들기\
    chess = [
        [0] * I
        for _ in range(I)
    ]
    #구현
    deq.append([a, b])
    chess[a][b] = 0

    while deq:
        popList = deq.popleft()
        x, y = popList[0], popList[1]
        if x == c and y == d:
            print(chess[x][y])
            break
        if (x - 2) >= 0 and (y - 1) >= 0 and chess[x - 2][y - 1] == 0:
            deq.append([x - 2, y - 1])
            chess[x - 2][y - 1] = chess[x][y] + 1
        if (x - 2) >= 0 and (y + 1) < I and chess[x - 2][y + 1] == 0:
            deq.append([x - 2, y + 1])
            chess[x - 2][y + 1] = chess[x][y] + 1
        if (x - 1) >= 0 and (y - 2) >= 0 and chess[x - 1][y - 2] == 0:
            deq.append([x - 1, y - 2])
            chess[x - 1][y - 2] = chess[x][y] + 1
        if (x + 1) < I and (y - 2) >= 0 and chess[x + 1][y - 2] == 0:
            deq.append([x + 1, y - 2])
            chess[x + 1][y - 2] = chess[x][y] + 1
        if (x + 2) < I and (y - 1) >= 0 and chess[x + 2][y - 1] == 0:
            deq.append([x + 2, y - 1])
            chess[x + 2][y - 1] = chess[x][y] + 1
        if (x + 2) < I and (y + 1) < I and chess[x + 2][y + 1] == 0:
            deq.append([x + 2, y + 1])
            chess[x + 2][y + 1] = chess[x][y] + 1
        if (x - 1) >= 0 and (y + 2) < I and chess[x - 1][y + 2] == 0:
            deq.append([x - 1, y + 2])
            chess[x - 1][y + 2] = chess[x][y] + 1
        if (x + 1) < I and (y + 2) < I and chess[x + 1][y + 2] == 0:
            deq.append([x + 1, y + 2])
            chess[x + 1][y + 2] = chess[x][y] + 1



