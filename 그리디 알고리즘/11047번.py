import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N, K = map(int, input().split())
lst = []

for _ in range(N):
    lst.append(int(input()))
lst = lst[::-1]

cnt = 0
for n in lst:
    if n <= K:
        cnt += (K // n)
        K %= n
    if K == 0:
        break

print(cnt)
