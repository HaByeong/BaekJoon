import sys
input = lambda : sys.stdin.readline().rstrip()

#나의 풀이 -> 내 풀이가 정석!
K = int(input())
Stack = []

Stack.append(int(input()))
for _ in range(K - 1):
    num = int(input())
    if num == 0:
        Stack.pop()
    else:
        Stack.append(num)
print(sum(Stack))
