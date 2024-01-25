import sys
import math
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이 -> 성공
N = int(input())
woodList = []

firstNum = int(input())
woodList.append(0)
for _ in range(N - 1):
    woodList.append(int(input()) - firstNum)

betList = []
for i in range(N - 1):
    betList.append(woodList[i + 1] - woodList[i])
num = math.gcd(*betList)

cnt = (woodList[N - 1] - woodList[0]) // num - 1
print(cnt + 2 - len(woodList))























