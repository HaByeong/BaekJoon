import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
numList = input().split('-')
ansList = []

for i in numList:
    if '+' in i:
        sum = 0
        list = i.split('+')
        for j in list:
            sum += int(j)
        ansList.append(sum)
    else:
        ansList.append(int(i))

sum = ansList[0]
for i in range(1, len(ansList)):
    sum -= ansList[i]
print(sum)


