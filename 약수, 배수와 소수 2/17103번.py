import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
def eratosprime(T):
    primeList = [True] * (T + 1)
    primeList[0] = primeList[1] = False

    for i in range(2, int(T ** 0.5) + 1):
        if primeList[i]:
            for j in range(i * 2, T + 1, i):
                primeList[j] = False
    return primeList

primeList = eratosprime(1000000)
T = int(input())

for _ in range(T):
    n = int(input())
    cnt = 0
    # 아래 방식에 대해 잘 고민해보자 (범위랑 두 개의 소수 합이라면 하나를 뺏을때도 소수가 되야하는 것)
    for i in range(2, n // 2 + 1):
        if primeList[i] and primeList[n - i]:
            cnt += 1
    print(cnt)

