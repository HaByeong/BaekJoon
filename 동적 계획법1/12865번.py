import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
#N은 물품 수, K는 버틸 수 있는 무게
N, K = map(int, input().split())
myBag = [0] * (K + 1)

for _ in range(N):
    #W는 물건의 무게, V는 물건의 가치
    W, V = map(int, input().split())
    for i in range(K, W - 1, -1):
        myBag[i] = max(myBag[i], myBag[i - W] + V)
print(max(myBag))



