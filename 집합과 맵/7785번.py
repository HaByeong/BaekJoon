import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
n = int(input())
userDict = {}

for _ in range(n):
    name, state = input().split()
    userDict[name] = state
    if userDict[name] == "leave":
        del userDict[name]

userList = list(userDict)
userList.sort(reverse = True)

for name in userList:
    print(name)

#정석 풀이
n = int(input())
userDict = dict()

for _ in range(n):
    name, state = input().split()
    if state == 'enter':
        userDict[name] = 1
    else:
        del userDict[name]

userList = list(userDict.keys())
userList.sort(reverse = True)

for name in userList:
    print(name)