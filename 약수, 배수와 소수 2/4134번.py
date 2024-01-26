import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이 -> 내가 정석!! 특정 숫자의 제곱근까지만 약수 여부 검증
def isPrimeNum(x):
    if x < 2:
        return False
    num = int(x ** 0.5)
    for i in range(2, num + 1):
        if x % i == 0:
            return False
    return True

N = int(input())

for _ in range(N):
    n = int(input())
    while isPrimeNum(n) == False:
        n += 1
    print(n)


