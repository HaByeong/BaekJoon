import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = int(input())
numList = list(map(int, input().split()))
lis = [0] * N
lis[0] = 1
lds = [0] * N
lds[0] = 1
lis_lds = [0] * N

#이게 이제 lis
for i in range(1, N):
    for j in range(i):
        if numList[i] > numList[j]:
            lis[i] = max(lis[i], lis[j])
    lis[i] += 1

#lds -> 이거 사실 그냥 numList를 반대로해서 나오는거 값을 반대로하는거랑 다를 바 없지 않나?
numList = numList[::-1]
for i in range(1, N):
    for j in range(i):
        if numList[i] > numList[j]:
            lds[i] = max(lds[i], lds[j])
    lds[i] += 1
lds = lds[::-1]

#lis + 문자 + lds 이건 위에 lis + lds의 리스트에 1을 빼면 된다
lis_lds = [lis[x] + lds[x] - 1 for x in range(N)]

#정답
print(max(max(lis), max(lds), max(lis_lds)))

