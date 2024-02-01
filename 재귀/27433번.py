import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)

N = int(input())
print(factorial(N))