import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
def canto_set(x):
    num = len(x)
    if num < 3:
        return x
    n = int(num / 3)
    x[n : 2 * n] = [" "] * n
    return canto_set(x[:n]), canto_set(x[2 * n :])


N = int(input())
L = ["-"] * 3 ** N

canto_set(L)
print(''.join(L))