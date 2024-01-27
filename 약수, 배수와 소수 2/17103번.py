import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
def eratosprime(T):
    primeList = [True] * (T + 1)
    primeList[0] = primeList[1] = False

    for i in range(2, T + 1):
        if primeList[i]:
            for j in range(i * 2, T + 1, i):
                primeList[j] = False

    prime = [i for i in range(T + 1) if primeList[i]]
    return prime

T = int(input())

for _ in range(T):
    N = int(input())
    primeList = eratosprime(N)
    cnt = 0
    n = len(primeList)
    for i in range(n - 1):
        if N // primeList[i] == 2 and N % primeList[i] == 0:
            cnt += 1
        for j in range(i + 1, n):
            sumVal = primeList[i] + primeList[j]
            if sumVal == N:
                cnt += 1
    if N // primeList[n - 1] == 2 and N % primeList[n - 1] == 0:
        cnt += 1
    print(cnt)