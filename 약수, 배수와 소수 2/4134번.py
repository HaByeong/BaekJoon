import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = int(input())

for _ in range(N):
    n = int(input())
    while True:
        cnt = 0
        for i in range(2, n):
            if n % i == 0:
                cnt += 1
        if cnt == 0:
            break
        n += 1
    print(n)

