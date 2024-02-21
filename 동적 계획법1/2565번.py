import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
numList = [0] * 501
lis = [0] * 501
N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    numList[a] = b

for i in range(1, 501):
    ##선택되지 않은 애들은 제외
    if numList[i] != 0:
        for j in range(i):
            if numList[i] > numList[j]:
                lis[i] = max(lis[j], lis[i])
        lis[i] += 1

print(N - max(lis))