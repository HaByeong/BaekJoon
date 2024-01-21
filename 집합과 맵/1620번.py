import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N, M = map(int, input().split())
monster1 = dict()
monster2 = dict()

for i in range(1, N + 1):
    word = input()
    monster1[str(i)] = word
    monster2[word] = i

for i in range(M):
    word = input()
    if word.isdigit():
        print(monster1[word])
    else:
        print(monster2[word])

#정석 풀이
N, M = map(int, input().split())
monster1 = dict()
monster2 = dict()

for i in range(N):
    PoketMon = input()
    monster1[str(i + 1)] = PoketMon
    monster2[PoketMon] = i + 1

for i in range(M):
    word = input()
    if word.isdigit():
        print(monster1[word])
    else:
        print(monster2[word])