import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = int(input())
numList = input().split()
numList2 = dict()

for i in numList:
    if i in numList2:
        numList2[i] += 1
    else:
        numList2[i] = 1

M = int(input())
answerList = input().split()

for i in answerList:
    if i in numList2.keys():
        print(numList2[i], end = " ")
    else:
        print(0, end = " ")

#정석 풀이 -> get() 사용하기

N = int(input())
numList = input().split()
M = int(input())
answerList = input().split()

d1 = dict()
for i in numList:
    if d1.get(i) == None:
        d1[i] = 1
    else:
        d1[i] += 1

for i in answerList:
    if d1.get(i) == None:
        print(0, end = " ")
    else:
        print(d1[i], end = " ")





