import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N, M = map(int, input().split())
numList = [
    [0] * (N + 1)
]

for i in range(N):
    row = [0] + [int(x) for x in input().split()]
    numList.append(row)

alst = [
    [0] * (N + 1)
    for _ in range(N + 1)
]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        alst[i][j] = alst[i - 1][j] + alst[i][j - 1] - alst[i - 1][j - 1] + numList[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    sum = alst[x2][y2] - alst[x1 - 1][y2] - alst[x2][y1 - 1] + alst[x1 - 1][y1 - 1]
    print(sum)