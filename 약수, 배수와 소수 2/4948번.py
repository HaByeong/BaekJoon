import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이 -> 애라토스테네스 체를 사용하는 건 맞고 사실 다른 코드는 개인 취향인듯
def eratosPrime(x):
    n = 2 * x + 1
    primeLists = [True] * n
    primeLists[0] = primeLists[1] = False

    for i in range(2, n):
        if primeLists[i]:
            for j in range(2 * i, n, i):
                primeLists[j] = False

    primeList = [i for i in range(n) if primeLists[i]]
    return primeList

while True:
    n = int(input())
    if n == 0:
        break
    primeList = eratosPrime(n)

    cnt = 0
    for i in primeList:
        if n < i:
            cnt += 1
    print(cnt)

