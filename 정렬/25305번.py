import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N, K = map(int, input().split())
scoreList = list(map(int, input().split()))

newList = sorted(scoreList, reverse = True)
#scoreList.sort(reverse = True) 해도 된다.
print(newList[K - 1])

#정석 풀이
#내가 곧 정석이다!!

