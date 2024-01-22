import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이 -> 근데 내 풀이가 시간이 제일 짧게 걸림..
N, M = map(int, input().split())

hearSet = set()
seeSet = set()

for _ in range(N):
    hearName = input()
    hearSet.add(hearName)

for _ in range(M):
    seeName = input()
    if seeName in hearSet:
        seeSet.add(seeName)

hearlookList = sorted(list(seeSet))

print(len(hearlookList))
for i in hearlookList:
    print(i)

#정석 풀이 -> 그냥 교집합을 이용해도 오케이! (intersection())

N, M = map(int, input().split())

hearSet = set()
seeSet = set()

for _ in range(N):
    name = input()
    hearSet.add(name)

for _ in range(M):
    name = input()
    seeSet.add(name)

intersectSet = hearSet.intersection(seeSet)
intersectList = sorted(list(intersectSet))

print(len(intersectList))

for i in intersectList:
    print(i)

# 아니면
N, M = map(int, input().split())

hearList = [0] * N
seeList = [0] * M

for i in range(N):
    hearList[i] = input()
for i in range(M):
    seeList[i] = input()

seehearList = sorted(list(set(hearList) & set(seeList)))
print(len(seehearList))
for name in seehearList:
    print(name)
