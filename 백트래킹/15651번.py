import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
def DFS(num, lst):
    if num == M:
        ans.append(lst)
        return
    for i in range(1, N + 1):
        DFS(num + 1, lst + [i])


N, M = map(int, input().split())
ans = []
DFS(0, [])
for i in ans:
    print(*i)