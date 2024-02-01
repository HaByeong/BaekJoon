import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return fibo(x - 2) + fibo(x - 1)

N = int(input())
print(fibo(N))