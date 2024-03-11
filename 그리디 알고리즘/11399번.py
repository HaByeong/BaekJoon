import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = int(input())
timeList = list(map(int, input().split()))
timeList.sort()
result = []

sum = timeList[0]
answer = timeList[0]
result.append(sum)

for i in range(1, N):
    sum += timeList[i]
    answer += sum
print(answer)

