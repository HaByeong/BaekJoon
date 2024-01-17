import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = input()
numList = []

for word in N:
    numList.append(int(word))

numList.sort(reverse = True)

for n in numList:
    print(n, end = "")

#정석 풀이
N = list(map(int, input()))
N.sort(reverse = True)

for i in N:
    print(i, end = "")
