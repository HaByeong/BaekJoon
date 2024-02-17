import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
lst = [0, 1, 2]
N = int(input())

for i in range(3, N + 1):
    ans = lst[i - 1] + lst[i - 2]
    lst.append(ans % 15746)
print(lst[N])





