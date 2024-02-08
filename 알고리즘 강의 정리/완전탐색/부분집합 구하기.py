#부분집합 구하기(DFS)
import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
def DFS(x):
    if x >= N + 1:
        for i in range(N + 1):
            if visit[i] == 1:
                print(i, end = " ")
        print()
        return
    else:
        visit[x] = 1
        DFS(x + 1)
        visit[x] = 0
        DFS(x + 1)

N = int(input())
visit = [0] * (N + 1)

DFS(1)
