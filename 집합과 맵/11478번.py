import sys
from itertools import combinations
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
S = input()
wordSet = set()

n = len(S)
for i in range(1, n + 1): #몇개 선택
    for j in range(n + 1 - i): #부분 집합 개수
        wordSet.add(S[j : j + i])
print(len(wordSet))

#정석 풀이
S = input()
S1 = set()

for i in range(len(S)):
    for j in range(i, len(S) + 1):
        S1.add(S[i : j])
print(len(S1) - 1)
























