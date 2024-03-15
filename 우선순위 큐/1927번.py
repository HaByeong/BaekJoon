import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = int(input())
heap = []

for i in range(N):
    x = int(input())
    #x가 0이라면 배열에서 가장 작은 값을 출력 후 제거, 자연수라면 배열에 x라는 값을 넣는 연산
    if x == 0 and len(heap) == 0:
        print(0)
    elif x == 0:
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)

