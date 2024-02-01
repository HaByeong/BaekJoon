import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = int(input())
numList = []
numDict = dict()
mostNum = []

#입력 수 오름차순으로 정렬
for _ in range(N):
    n = int(input())
    numList.append(n)
numList.sort()

#최빈값을 구하기 위한 노력..
for i in numList:
    if i not in numDict:
        numDict[i] = 0
    else:
        numDict[i] += 1
maxVal = max(numDict.values())

for i in numDict:
    if numDict[i] == maxVal:
        mostNum.append(i)
mostNum.sort()

#산술 평균
answer = round((sum(numList) / N))
print(answer)
#중앙값
print(numList[N // 2])
#최빈값
if len(mostNum) == 1:
    print(mostNum[0])
else:
    print(mostNum[1])
#범위
print(numList[-1] - numList[0])