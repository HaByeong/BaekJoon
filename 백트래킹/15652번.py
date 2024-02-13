import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
def DFS(num, lst, cnt):
    if num == M:
        ans.append(lst)
        return
    if cnt > 0:
        for i in range(cnt, N + 1):
            DFS(num + 1, lst + [i], i)

N, M = map(int, input().split())
ans = []
DFS(0, [], 1)
for i in ans:
    print(*i)