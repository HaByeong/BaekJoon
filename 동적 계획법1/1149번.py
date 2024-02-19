import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이 -> 어차피 본인 기준 합에서는 자기 이전 부분 자기 위치가 아닌 두 개 중에 더한 합이 작은 애가 계속 쭉 작은 합일 수 밖에 없음
N = int(input())
lst = [
    list(map(int, input().split()))
    for _ in range(N)
]
ans = [
    [0] * 3
    for _ in range(N)
]


for i in range(N):
    for j in range(3):
        if i == 0:
            ans[i][j] = lst[i][j]
        elif j == 0:
            ans[i][j] = min(ans[i - 1][j + 1] + lst[i][j], ans[i - 1][j + 2] + lst[i][j])
        elif j == 1:
            ans[i][j] = min(ans[i - 1][j + 1] + lst[i][j], ans[i - 1][j - 1] + lst[i][j])
        elif j == 2:
            ans[i][j] = min(ans[i - 1][j - 1] + lst[i][j], ans[i - 1][j - 2] + lst[i][j])

print(min(ans[N - 1][0], ans[N - 1][1], ans[N - 1][2]))
        

