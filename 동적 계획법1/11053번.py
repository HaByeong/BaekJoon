import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = int(input())
lst = list(map(int, input().split()))
lst.insert(0, 0)
lis = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(i):
        if lst[i] > lst[j]:
            lis[i] = max(lis[i], lis[j])
    lis[i] += 1

print(max(lis))