#내 풀이
N = int(input())
cnt = 1
numAll = 1

while True:
    beeMap = (6 * (cnt - 1))
    numAll += beeMap
    if N <= numAll:
        break
    cnt += 1

print(cnt)

#정석 풀이
#등차수열 합 공식 써라!