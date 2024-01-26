import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이 -> 애라토스테네스 체를 사용하자!!!
def eratosthenes(N):
    #모든 수를 소수로 가정
    isPrime = [True] * (N + 1)
    #0과 1은 제외
    isPrime[0] = isPrime[1] = False

    # 에라토스테네스 알고리즘
    for i in range(2, N + 1):
        if isPrime[i] == True:
            for j in range(i * 2, N + 1, i):
                isPrime[j] = False
    # 소수 저장
    primes = [i for i in range(N + 1) if isPrime[i]]
    return primes

M, N = map(int, input().split())

primeList = eratosthenes(N)

for i in primeList:
    if i >= M:
        print(i)