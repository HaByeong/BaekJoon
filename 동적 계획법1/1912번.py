import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
n = int(input())
lst = list(map(int, input().split()))

checkNum = 0
ans = set()

for i in range(n):
    #그냥 처음값 or checkNum == 0인 -> sumValue가 - 이면 sumValue를 자기 자신으로
    if i == 0 or checkNum == 0:
        sumValue = lst[i]
        ans.add(sumValue)
    else:
        sumValue += lst[i]
    if sumValue >= 0:
        checkNum = 1
        ans.add(sumValue)
    else:
        checkNum = 0
        ans.add(sumValue)
print(max(ans))








