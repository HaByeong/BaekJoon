import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
def hanoi(num, start, end, sub):
    if num == 0:
        return
    hanoi(num - 1, start, sub, end)
    print(start, end)
    hanoi(num - 1, sub, end, start)

N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 3, 2)