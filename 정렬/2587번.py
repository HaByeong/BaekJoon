import sys
#람다 함수!
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
numList = []
sum_val = 0

for _ in range(5):
    numList.append(int(input()))

numList.sort()

print(int(sum(numList) / 5))
print(numList[2])

#정석 풀이 => sort() 말고 sorted 사용(연산 시간이 더 빠름)
numList = []
sum_val = 0

for _ in range(5):
    numList.append(int(input()))

newList = sorted(numList)

print(int(sum(newList) / 5))
print(newList[2])