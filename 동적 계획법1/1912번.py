import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
n = int(input())
lst = list(map(int, input().split()))
#sumValue가 지금 +인지, -인지 확인(+면 1, -면 0)
checkNum = 0
ans = set()

for i in range(n):
    #그냥 처음값 or checkNum == 0인 -> sumValue가 - 이면(연속 합 최대 이탈) sumValue를 자기 자신으로
    if i == 0 or checkNum == 0:
        sumValue = lst[i]
        ans.add(sumValue)
    else:
        sumValue += lst[i]
    if sumValue >= 0:
        checkNum = 1
        ans.add(sumValue)
    else:
        #sumValue가 -가 되면 그 다음 시점부터 다시 sumValue를 구할 것이야
        checkNum = 0
        ans.add(sumValue)
print(max(ans))








