import sys
input = sys.stdin.readline

#나의 풀이
N = int(input())
numList = []

for _ in range(N):
    numList.append(int(input()))

numList.sort()

for n in numList:
    print(n)

#정석 풀이
#내가 정석이다!