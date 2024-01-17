#나의 풀이
n = int(input())
numAll = 1
numVal = 0

while True:
    num = str(numAll)[::-1]
    cnt = 0

    for word in num:
        if word == '6':
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            numVal += 1
            break

    if numVal == n:
        print(numAll)
        break

    numAll += 1

# 정석 풀이
N = int(input())
name = 665

while 0 < N:
    name += 1
    if "666" in str(name):
        N -= 1
print(name)




