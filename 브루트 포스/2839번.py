import sys
input = sys.stdin.readline

# 나의 풀이
N = int(input())
numList = []

for i in range(1001):
    for j in range(2000):
        num = 5 * i + 3 * j
        if num == N:
            numList.append(i + j)
        if num > N:
            break

if len(numList) == 0:
    print(-1)
else:
    print(min(numList))

# 정석 풀이
N = int(input())
cnt = 0

while N >= 0:
    if N % 5 == 0:
        cnt += N // 5
        print(cnt)
        break
    N -= 3
    cnt += 1
else:
    print(-1)


