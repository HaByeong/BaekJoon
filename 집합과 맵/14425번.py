import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N, M = map(int, input().split())
cnt = 0
wordList = []

for _ in range(N):
    wordList.append(input())

wordSet = set(wordList)

for _ in range(M):
    if input() in wordSet:
        cnt += 1

print(cnt)

#정석 풀이 set()을 사용하는 법
N, M = map(int, input().split())
wordSet = set()

for _ in range(N):
    wordSet.add(input())

cnt = 0
for _ in range(M):
    if input() in wordSet:
        cnt += 1
print(cnt)