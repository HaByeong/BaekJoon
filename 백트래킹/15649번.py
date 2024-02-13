import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
#여기서 num은 수열의 길이다.
def DFS(num, lst):
    if num == M:
        ans.append(lst)
        return
    for i in range(1, N + 1):
        #여기가 문제다
        if i not in lst:
            DFS(num + 1, lst + [i])

#N까지 자연수까지 수열, 길이가 M인 수열
N, M = map(int, input().split())
ans = []
DFS(0, [])
for i in ans:
    print(*i)