import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = int(input())

num, cnt = 1, 0
while True:
    M = num ** 2
    if N < M:
        break
    num += 1
    cnt += 1
print(cnt)

