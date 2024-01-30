import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이 -> 그냥 약수(1과 자기 자신 빼고) 제일 작은 애랑 제일 큰 애 곱하면 본인임
N = int(input())
nList = list(map(int, input().split()))
nList.sort()

print(nList[0] * nList[-1])

#정석 풀이
N = int(input())
nList = list(map(int, input().split()))

print(max(nList) * min(nList))