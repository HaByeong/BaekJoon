import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
def hanoi(num, start, end, sub):
    if num == 1:
        print(start, end)
        return
    hanoi(num - 1, start, sub, end)
    print(start, end)
    hanoi(num - 1, sub, end, start)

def hanoi_num(n):
    if 2 ** n == 1:
        return 0
    return 2 ** (n - 1) + hanoi_num(n - 1)

N = int(input())
if N <= 20:
    print(hanoi_num(N))
    hanoi(N, 1, 3, 2)
else:
    print(hanoi_num(N))