import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이 -> 초기값 [1, 1, 1, 2, 2] 이후부터 (n - 1) + (n - 5)
lst = [0, 1, 1, 1, 2, 2]
for i in range(6, 101):
    ans = lst[i - 1] + lst[i - 5]
    lst.append(ans)

T = int(input())
for _ in range(T):
    N = int(input())
    print(lst[N])