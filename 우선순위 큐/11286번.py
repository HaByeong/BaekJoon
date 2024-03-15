import sys
import heapq as hq
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이 -> 나는 딕셔너리를 사용했다
heap = []
cnt = dict()
N = int(input())

for i in range(N):
    x = int(input())
    #-인 애들의 개수를 넣자
    if x < 0 and (x * -1) not in cnt:
        cnt[x * -1] = 1
    elif x < 0:
        cnt[x * -1] += 1
    if x == 0 and len(heap) == 0:
        print(0)
    elif x == 0:
        num = hq.heappop(heap)
        if num in cnt and cnt[num] > 0:
            print(num * -1)
            cnt[num] -= 1
        elif (num not in cnt) or cnt[num] < 1:
            print(num)

    else:
        hq.heappush(heap, abs(x))


#정석 풀이 -> 그냥 힙 우선순위 이용
heap = []
N = int(input())

for i in range(N):
    x = int(input())
    if x == 0 and len(heap) == 0:
        print(0)
    elif x == 0:
        print(hq.heappop(heap)[1]) # 우선 순위를 지정한 abs(x)가 아닌 그 우선 순위를 토대로 지정된 x의 값을 반환
    else:
        hq.heappush(heap, (abs(x), x))

