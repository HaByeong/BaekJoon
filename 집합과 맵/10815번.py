import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = int(input())
numSet = set(input().split())

M = int(input())
numList = input().split()


for j in range(M):
    if numList[j] in numSet:
        numList[j] = 1
    else:
        numList[j] = 0
    print(numList[j], end = " ")

#정석 풀이
N = int(input())
numSet = set(input().split())

M = int(input())
numList = input().split()

for i in numList:
    if i in numSet:
        print(1, end = " ")
    else:
        print(0, end = " ")
