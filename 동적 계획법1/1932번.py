import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = int(input())
lst = [
    list(map(int, input().split()))
    for _ in range(N)
]
ans = [
    [0] * i
    for i in range(1, N + 1)
]

for i in range(N):
    for j in range(i + 1):
        if i == 0:
            ans[i][j] = lst[i][j]
        elif j == 0:
            ans[i][j] = ans[i - 1][j] + lst[i][j]
        elif j == i:
            ans[i][j] = ans[i - 1][j - 1] + lst[i][j]
        else:
            ans[i][j] = max(ans[i - 1][j - 1], ans[i - 1][j]) + lst[i][j]
print(max(ans[N - 1]))

