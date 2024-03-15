import sys
import heapq as hq
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이
N = int(input())
heap = []

for i in range(N):
    x = int(input()) * (-1)
    if x == 0 and len(heap) == 0:
        print(0)
    elif x == 0:
        print(abs(hq.heappop(heap)))
    else:
        hq.heappush(heap, x)
