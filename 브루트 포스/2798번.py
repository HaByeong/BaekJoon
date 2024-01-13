#나의 풀이
N, M = map(int, input().split())
cardList = list(map(int, input().split()))

nearSum = 0
numSum = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            numSum = cardList[i] + cardList[j] + cardList[k]
            if nearSum < numSum <= M:
                nearSum = numSum
print(nearSum)

#나의 풀이가 정석