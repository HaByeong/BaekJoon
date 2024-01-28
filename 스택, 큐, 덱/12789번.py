import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

#나의 플이 -> 나는 스택이랑 그냥 구현함
N = int(input())
numList1 = list(map(int, input().split()))
numList2 = []
Stack = []

cnt = 1
i = 0
while True:
    if cnt == numList1[i]:
        numList2.append(numList1[i])
        numList1.remove(numList1[i])
        cnt += 1
    else:
        if len(Stack) > 0 and Stack[-1] == cnt:
            numList2.append(Stack.pop())
            cnt += 1
        else:
            Stack.append(numList1[i])
            numList1.remove(numList1[i])
    if len(numList1) == 0:
        break

Stack2 = sorted(Stack, reverse = True)
if Stack  == Stack2:
    print("Nice")
else:
    print("Sad")

#정석 풀이 -> 스택과 큐를 사용
N = int(input())
Queue = deque(map(int, input().split()))
Stack = []

num = 1
while True:
    if Queue and num == Queue[0]:
        Queue.popleft()
        num += 1
    elif Stack and num == Stack[-1]:
        Stack.pop()
        num += 1
    elif Queue:
         n = Queue.popleft()
         Stack.append(n)
    else:
        break

if Queue or Stack:
    print("Sad")
else:
    print("Nice")





